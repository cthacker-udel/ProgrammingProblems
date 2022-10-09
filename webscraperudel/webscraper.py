import time
from pprint import pprint
import requests
from bs4 import BeautifulSoup, ResultSet
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import re
import json

ALL_COURSE_URL = 'https://udapps.nss.udel.edu/CoursesSearch/search-results?term=2228&search_type=A&course_sec=&session=All&course_title=&instr_name=&text_info=All&campus=&instrtn_mode=All&time_start_hh=&time_start_ampm=&credit=Any&keyword=&geneduc=&subj_area_code=&college='
not_available = 'N/A'
course_information = {}
searched_courses = []
cached_ed_breadth_results = {}


campus_mapping = {
    'NEWRK': 'Newark',
    'DOVER': 'Dover',
    'GTOWN': 'Georgetown',
    'LEWES': 'Lewes',
    'WILM': 'Wilmington',
}

course_mapping = {
    'M': 'Monday',
    'T': 'Tuesday',
    'W': 'Wednesday',
    'TR': 'Thursday',
    'F': 'Friday',
}

location_mapping = {
    'GOR': 'Gore',
    'PRN': 'Purnell',
    'ALS': 'Alison',
    'LEH': 'Alfred Lerner',
    'MDH': 'McDowell',
    'MEM': "Memorial",
    'SPL': 'Spencer Lab',
    'WHL': 'Willard'
}


def generate_search_endpoint(prefix):
    return f'term=2228&search_type={prefix}&course_sec={prefix}&session=All&course_title=&instr_name=&text_info=All&campus=&instrtn_mode=All&time_start_hh=&time_start_ampm=&credit=Any&keyword=&geneduc=&subj_area_code=&college='


def parse_course_name(name: str):
    """
    Arguments:
        name: the parsed course name, will come in like ACCT200010, and we parse it into it's respective parts
            [ACCT, 200, 010], the name, course number, and section
    Returns:
        The parsed course name, into it's name, number, and section
    """
    name_ = ''
    number_ = ''
    section_ = ''
    is_number = False
    for i in range(len(name)):
        if is_number and name[i].isdigit():
            if len(number_) == 3:
                section_ += name[i]
            else:
                number_ += name[i]
        else:
            name_ += name[i]
            if i < len(name) - 1:
                is_number = name[i + 1].isdigit()
    return [name_, number_, section_]


def parse_course_days(daystr: str):
    """
    Arguments:
        daystr - The string of the day, MWF, TR, R, etc

    Returns:
        The parsed daystr, which will be an array of the days ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    """
    course_days = []
    if 'M' in daystr:
        course_days.append(course_mapping['M'])
    if 'W' in daystr:
        course_days.append(course_mapping['W'])
    if 'F' in daystr:
        course_days.append(course_mapping['F'])
    if 'TR' in daystr:
        course_days.append(course_mapping['TR'])
    return course_days


def parse_course_time(timestr: str):
    """
    Arguments:
        timestr - The string of the time of the course, 3:30PM - 5:15PM
    Returns:
        The parsed time of the course, [lower, upper] bounds
    """
    split_timestr = timestr.split(' - ')
    left_bound = split_timestr[0]
    right_bound = split_timestr[1]
    if '\n' in right_bound:
        _ind = right_bound.index('\n')
        right_bound = right_bound[0:_ind].strip()
        right_bound = right_bound.replace(
            'AM' if 'AM' in right_bound else 'PM', '')
    is_am = 'AM' in right_bound
    return [left_bound, right_bound, is_am]


def parse_course_location(locationstr: str):
    """
    Arguments:
        locationstr - The string of the location of the course
    Returns:
        The parsed location string
    """
    room = ''
    loc = ''
    for eachletter in locationstr:
        if eachletter.isdigit():
            room += eachletter
        else:
            loc += eachletter
    return [location_mapping[loc] if loc in location_mapping else loc, room]


def main():
    base_url = 'https://udapps.nss.udel.edu/CoursesSearch/'
    firefox_scraper = webdriver.Firefox(
        executable_path=GeckoDriverManager().install())
    firefox_scraper.get(
        "https://catalog.udel.edu/content.php?catoid=63&navoid=16384")
    course_code_input = None
    course_code_keyword = None
    course_code_filter_button = None
    course_code_select = None
    time.sleep(2)



    next_button = None
    started_searching = False
    page = requests.get('{}'.format(
        ALL_COURSE_URL))

    while (not next_button and not started_searching) or (next_button):
        if not started_searching:
            started_searching = True
        elif started_searching and next_button:
            appended_url = next_button['onclick'].replace(
                'location.href=\'', '').replace('\'', '')[:-1]
            full_url = f'{base_url}{appended_url}'
            page = requests.get('{}'.format(full_url))

        while (not page):
            pass
        soup = BeautifulSoup(page.content, "html.parser")
        rows = soup.tbody
        if rows:
            rows = rows.find_all('tr')
        else:
            rows = []
        next_button = soup.find(id='searchNxtBtn')
        name = ''
        number = ''
        section = ''
        course_title = ''
        course_campus = ''
        course_total_seats = ''
        course_credits = ''
        course_day = ''
        course_time = ''
        course_location = ''
        course_teacher = ''
        course_prereqs = []
        course_prereqs_or = False
        course_coreqs = []
        course_coreqs_or = False
        course_educational_objectives = []
        course_breadth_requirements = {}

        for eachrow in rows:
            try:
                firefox_scraper.find_element(
                    By.ID, 'coursenumber').clear()
            except:
                pass
            try:
                firefox_scraper.find_element(
                    By.ID, 'course_filter_keyword').clear()
            except:
                pass
            name = ''
            number = ''
            section = ''
            course_title = ''
            course_campus = ''
            course_total_seats = ''
            course_credits = ''
            course_day = ''
            course_time = ''
            course_location = ''
            course_teacher = ''
            course_prereqs = []
            course_prereqs_or = False
            course_coreqs = []
            course_coreqs_or = False
            course_educational_objectives = []
            course_breadth_requirements = {}
            try:
                [name, number, section] = parse_course_name(
                    eachrow.find('td', class_='course').a.text)
            except:
                name = not_available
                number = not_available
                section = not_available
            try:
                course_title = eachrow.contents[3].text.strip().split('  ')[
                    0].strip()
            except:
                course_title = not_available
            try:
                course_campus = campus_mapping[eachrow.find(
                    'td', class_='campus').text.strip()]
            except:
                course_campus = not_available
            try:
                course_total_seats = eachrow.find(
                    'td', class_='openseats').text.strip().replace('CURRENTLY FULL', '').split(' OF ')[1].strip()
            except:
                course_total_seats = not_available
            try:
                course_credits = eachrow.find(
                    'td', string=re.compile('Hrs')).text.strip().split(' Hrs')[0]
            except:
                course_credits = not_available
            try:
                course_day = parse_course_days(
                    eachrow.find('td', class_='day').text.strip())
            except:
                course_day = not_available
            try:
                course_time = parse_course_time(
                    eachrow.find('td', class_='time').text.strip())
            except:
                course_time = not_available
            try:
                course_location = parse_course_location(
                    eachrow.find('td', class_='location').a.text.strip())
            except:
                course_location = not_available
            try:
                teacher_newline_index = eachrow.contents[len(eachrow.contents) - 4].text.strip().index('\n')
                course_teacher = eachrow.contents[len(
                    eachrow.contents) - 4].text.strip()[:teacher_newline_index].strip()
            except:
                course_teacher = not_available
            stored_result = {}
            stored_result['name'] = name
            stored_result['number'] = number
            stored_result['section'] = section
            stored_result['title'] = course_title
            stored_result['campus'] = course_campus
            stored_result['total_seats'] = course_total_seats
            stored_result['credits'] = course_credits
            stored_result['day'] = course_day
            stored_result['course_time'] = course_time
            stored_result['location'] = course_location
            stored_result['teacher'] = course_teacher
            try:
                course_detail_link = eachrow.find_all(
                    'a', class_='coursenum')[0]['href']
                url_ = f'{base_url}{course_detail_link}'.replace(
                    ' // ', '//').replace('§ion', '&section')
                course_detail_page = requests.get(
                    url_)
                souped_content = BeautifulSoup(
                    course_detail_page.content, 'html.parser')
                pre_req_paragraphs = souped_content.find_all(
                    'p', string=re.compile('PREREQ|Prerequisites'))
                for eachsoupparagraph in pre_req_paragraphs:
                    if 'PREREQ' in eachsoupparagraph.text:
                        eachparagraph = eachsoupparagraph.text
                        capital_ind = eachparagraph.index('PREREQ')
                        capital_start = eachparagraph[capital_ind + 6:]
                        capital_second_start = capital_start.index(name)
                        capital_start = capital_start[capital_second_start:]
                        capital_end_index = capital_start.index('.')
                        capital_substr = capital_start[0:capital_end_index]
                        if 'or' in capital_substr:
                            split_ors = capital_substr.split(' or ')
                            for eachclass in split_ors:
                                if eachclass not in course_prereqs:
                                    course_prereqs.append(eachclass.strip())
                            course_prereqs_or = True
                        elif 'and' in capital_substr:
                            split_and = capital_substr.split(' and ')
                            for eachclass in split_and:
                                if eachclass not in course_prereqs:
                                    course_prereqs.append(eachclass.strip())
                        elif ', ' in capital_substr:
                            split_comma = capital_substr.split(', ')
                            for eachclass in split_comma:
                                course_prereqs.append(eachclass.strip())
                        else:
                            capital_substr = capital_substr.strip()
                            if capital_substr not in course_prereqs:
                                course_prereqs.append(capital_substr)
                    elif 'Prerequisites' in eachparagraph.text:
                        lowercase_ind = eachparagraph.index('Prerequisites:')
                        capital_start = eachparagraph[lowercase_ind + 14:]
                        capital_second_start = capital_start.index(name)
                        capital_start = capital_start[capital_second_start:]
                        capital_end_index = capital_start.index('.')
                        capital_substr = capital_start[0:capital_end_index]
                        if 'or' in capital_substr:
                            split_ors = capital_substr.split(' or ')
                            for eachclass in split_ors:
                                if eachclass not in course_prereqs:
                                    course_prereqs.append(eachclass.strip())
                            course_prereqs_or = True
                        elif 'and' in capital_substr:
                            split_and = capital_substr.split(' and ')
                            for eachclass in split_and:
                                if eachclass not in course_prereqs:
                                    course_prereqs.append(eachclass.strip())
                        elif ', ' in capital_substr:
                            split_comma = capital_substr.split(', ')
                            for eachclass in split_comma:
                                course_prereqs.append(eachclass.strip())
                        else:
                            capital_substr = capital_substr.strip()
                            if capital_substr not in course_prereqs:
                                course_prereqs.append(capital_substr)
                if len(course_prereqs) > 0:
                    course_prereqs.append(course_prereqs_or)
            except:
                pass
            try:
                coreq_paragraphs = souped_content.find_all(
                    'p', string=re.compile('COREQ|Corequisites'))
                for eachsoupparagraph in coreq_paragraphs:
                    if 'COREQ' in eachsoupparagraph.text:
                        eachparagraph = eachsoupparagraph.text
                        capital_ind = eachparagraph.index('COREQ')
                        capital_start = eachparagraph[capital_ind + 6:]
                        capital_second_start = capital_start.index(name)
                        capital_start = capital_start[capital_second_start:]
                        capital_end_index = capital_start.index('.')
                        capital_substr = capital_start[0:capital_end_index]
                        if 'or' in capital_substr:
                            split_ors = capital_substr.split(' or ')
                            for eachclass in split_ors:
                                if eachclass not in course_coreqs:
                                    course_coreqs.append(eachclass.strip())
                            course_coreqs_or = True
                        elif 'and' in capital_substr:
                            split_and = capital_substr.split(' and ')
                            for eachclass in split_and:
                                if eachclass not in course_coreqs:
                                    course_coreqs.append(eachclass.strip())
                        elif ', ' in capital_substr:
                            split_comma = capital_substr.split(', ')
                            for eachclass in split_comma:
                                course_coreqs.append(eachclass.strip())
                        else:
                            capital_substr = capital_substr.strip()
                            if capital_substr not in course_coreqs:
                                course_coreqs.append(capital_substr)
                    elif 'Corequisites' in eachparagraph.text:
                        lowercase_ind = eachparagraph.index('Corequisites:')
                        capital_start = eachparagraph[lowercase_ind + 14:]
                        capital_second_start = capital_start.index(name)
                        capital_start = capital_start[capital_second_start:]
                        capital_end_index = capital_start.index('.')
                        capital_substr = capital_start[0:capital_end_index]
                        if 'or' in capital_substr:
                            split_ors = capital_substr.split(' or ')
                            for eachclass in split_ors:
                                if eachclass not in course_coreqs:
                                    course_coreqs.append(eachclass.strip())
                            course_coreqs_or = True
                        elif 'and' in capital_substr:
                            split_and = capital_substr.split(' and ')
                            for eachclass in split_and:
                                if eachclass not in course_coreqs:
                                    course_coreqs.append(eachclass.strip())
                        elif ', ' in capital_substr:
                            split_comma = capital_substr.split(', ')
                            for eachclass in split_comma:
                                course_coreqs.append(eachclass.strip())
                        else:
                            capital_substr = capital_substr.strip()
                            if capital_substr not in course_coreqs:
                                course_coreqs.append(capital_substr)
                if len(course_coreqs) > 0:
                    course_coreqs.append(course_coreqs_or)
            except:
                pass
            stored_result['prereqs'] = course_prereqs
            stored_result['coreqs'] = course_coreqs
            if [name, number] not in searched_courses:
                try:
                    course_code_input = firefox_scraper.find_element(
                        By.ID, 'coursenumber')
                except:
                    course_code_input = None
                if course_code_input:
                    course_code_input.send_keys(number)
                searched_courses.append([name, number])
                try:
                    course_code_select = Select(
                        firefox_scraper.find_element(By.ID, "courseprefix"))
                except:
                    course_code_select = None
                if course_code_select:
                    try:
                        course_code_select.select_by_visible_text(name)
                    except:
                        course_code_keyword = firefox_scraper.find_element(
                            By.ID, "course_filter_keyword")
                        if course_code_keyword:
                            course_code_keyword.send_keys(name)
                try:
                    course_code_filter_button = firefox_scraper.find_element(
                        By.ID, 'search-with-filters')
                except:
                    course_code_filter_button = None
                if course_code_filter_button:
                    course_code_filter_button.click()

                time.sleep(5)
                course_info_available = False
                try:
                    course_link = firefox_scraper.find_element(
                        By.XPATH, "/html/body/table/tbody/tr[3]/td[2]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[2]/tbody/tr[3]/td[2]/a")
                    course_link.click()
                    course_info_available = True
                except:
                    course_info_available = False
                    break
                time.sleep(5)

                if course_info_available:
                    course_displayed_information = BeautifulSoup(
                        firefox_scraper.page_source, 'html.parser')

                    course_padding = course_displayed_information.find(
                        'td', class_='coursepadding', recursive=True)
                    if course_padding:
                        class_info = course_padding.contents[2]
                        class_info_contents = class_info.contents
                        ed_obj_found = False
                        requirement_designations_found = False
                        capstone_found = False
                        breadth_found = False
                        for i in range(len(class_info_contents)):
                            eachnode = class_info_contents[i]
                            if eachnode.text and 'Education Objectives' in eachnode.text.strip():
                                ed_obj_found = True
                            elif ed_obj_found and eachnode.name == 'br':
                                continue
                            elif ed_obj_found and eachnode.text and len(eachnode.text.strip()) > 0 and eachnode.text.strip() != 'Close':
                                split_objectives = re.split(
                                    'GE[0-9][a-zA-Z]?: ', eachnode.text)
                                for eachobjective in split_objectives:
                                    if len(eachobjective.strip()) > 0:
                                        course_educational_objectives.append(
                                            eachobjective.strip())
                                ed_obj_found = False
                        for i in range(len(class_info_contents)):
                            eachnode = class_info_contents[i]
                            if 'University Breadth' in eachnode.text:
                                breadth_found = True
                            elif 'Course Typically Offered' in eachnode.text:
                                break
                            elif breadth_found and 'Breadth' not in eachnode and len(eachnode.text.strip()) > 0:
                                if 'UNIV ' in course_breadth_requirements:
                                    course_breadth_requirements['UNIV'] = course_breadth_requirements['UNIV'] + [
                                        eachnode.text.strip()]
                                else:
                                    course_breadth_requirements['UNIV'] = [
                                        eachnode.text.strip()]
                    if course_code_input:
                        firefox_scraper.find_element(
                            By.ID, 'coursenumber').clear()
                    if course_code_keyword:
                        firefox_scraper.find_element(
                            By.ID, 'course_filter_keyword').clear()
                    cached_ed_breadth_results[f'{name}{number}'] = [
                        course_breadth_requirements, course_educational_objectives]
            elif f'{name}{number}' in cached_ed_breadth_results:
                course_breadth_requirements = cached_ed_breadth_results[f'{name}{number}'][0]
                course_educational_objectives = cached_ed_breadth_results[f'{name}{number}'][1]
            stored_result['breadth'] = course_breadth_requirements
            stored_result['education_objectives'] = course_educational_objectives
            stored_result['id'] = f'{name}{number}{section}'
            course_information[f'{name}{number}{section}'] = stored_result
    with open('courses.json', 'w') as outfile:
        output_array = []
        for eachkey in course_information:
            output_array.append(course_information[eachkey])
        json.dump(output_array, outfile)


if __name__ == '__main__':
    main()
