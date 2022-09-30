import time
from pprint import pprint
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup, ResultSet
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver

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
    'R': 'Friday'
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
        if not is_number and name.isdigit():
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
    elif 'W' in daystr:
        course_days.append(course_mapping['W'])
    elif 'F' in daystr:
        course_days.append(course_mapping['F'])
    elif 'TR' in daystr:
        course_days.append(course_mapping['TR'])
    elif 'R' in daystr and 'TR' not in daystr:
        course_days.append(course_mapping['R'])
    elif 'R' in daystr and daystr.count('R') == 2:
        course_days.append(course_mapping['R'])
    return course_days


def parse_course_time(timestr: str):
    """
    Arguments:
        timestr - The string of the time of the course, 3:30PM - 5:15PM
    Returns:
        The parsed time of the course, [lower, upper] bounds
    """
    split_timestr = timestr.replace('PM', '').split(' - ')
    left_bound = split_timestr[0]
    right_bound = split_timestr[1]
    return [left_bound, right_bound]


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
    base_url = 'https://udapps.nss.udel.edu/CoursesSearch/search-results'
    br = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    br.get('{}?{}'.format(base_url, generate_search_endpoint('A')))
    time.sleep(2)
    soup = BeautifulSoup(br.page_source, "html.parser")
    course_information = {}
    odd_rows: ResultSet = soup.find_all('tr', class_='odd')
    even_rows = soup.find_all('tr', class_='even')
    for eachrow in odd_rows:
        [name, number, section] = parse_course_name(eachrow.find(
            'a', class_='coursenum').string)
        print(eachrow.contents[3].string)
        print([name, number, section])
        # course_title = eachrow.children[1].text()
        # course_campus = eachrow.find('td', class_='campus').text().strip()
        # if course_campus in campus_mapping:
        #     course_campus = campus_mapping[course_campus]
        # course_credits = eachrow.children[4].text().replace('Hrs', '').strip()
        # course_days = parse_course_days(
        #     eachrow.find('td', class_='day').text().strip())
        # [start, end] = parse_course_time(
        #     eachrow.find('td', class_='time').text().strip())
        # course_location = parse_course_location(eachrow.find(
        #     'td', class_='location').children[0].text().strip())
        # course_information[name]: dict = {
        #     course_number: number,
        #     course_section: section,
        #     course_title: course_title,
        #     course_campus: course_campus,
        #     course_credits: int(course_credits),
        #     course_days: course_days,
        #     course_start_time: start,
        #     course_end_time: end,
        #     course_location: course_location,
        # }
    pprint(course_information)


if __name__ == '__main__':
    main()
