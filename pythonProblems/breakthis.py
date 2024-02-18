from datetime import datetime, timedelta

def get_first_day_of_week_after_date(start_date, day_of_week):
    #weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    current_date = start_date
    while current_date.strftime("%A").lower() != day_of_week.lower():
        current_date += timedelta(days=1)
    return current_date

def get_all_dates(start_date, end_date, delta_days=7):
    all_dates = []
    current_date = start_date
    while current_date <= end_date:
        all_dates.append(current_date)
        current_date += timedelta(days=delta_days)
    return all_dates

class OfficeHoursScheduler:
    def __init__(self, semester_start_date, semester_end_date, ta_schedule):
        self.semester_start_date = semester_start_date
        self.semester_end_date = semester_end_date
        self.office_hours = {} #self.office_hours[person_id][date] = []
        """
        Matt:{Jan 10th:[ {10am - 11am},{3pm - 4pm} ]
        max:{Jan 11th: [ {11am - 12pm}], Jan 18th: [ {11am - 12pm} ],  Jan 25th: [ {11am - 12pm} ]
        """

    #add_single_office_hour
    def add_single_office_hour(self, person_id, date, start_time, end_time, additional=False):
        if person_id not in self.office_hours:
            self.office_hours[person_id] = {}
        if date not in self.office_hours[person_id]:
            self.office_hours[person_id][date] = []
        # Check for duplicates before adding
        current_office_hours = self.office_hours[person_id][date]
        if {'start_time': start_time, 'end_time': end_time} not in current_office_hours:
            self.office_hours[person_id][date].append({'start_time': start_time, 'end_time': end_time})
            print(f"Added specific office hour for person {person_id} on {date} from {start_time} to {end_time}")
            if additional:
                pass #add to additional_office_hours list
        else:
            print(f"Office hour for person {person_id} on {date} at {start_time} to {end_time} already exists")

    #add_remaining_office_hours
    def add_remaining_office_hours(self, person_id, start_date, day_of_week, start_time, end_time):
        date_of_first_office_hours = get_first_day_of_week_after_date(start_date, day_of_week)
        for date in get_all_dates(date_of_first_office_hours, self.semester_end_date):
            self.add_single_office_hour(person_id, date, start_time, end_time)

    def add_office_hours(self, person_id, day_of_week, start_time, end_time):
        self.add_remaining_office_hours(person_id, self.semester_start_date, day_of_week, start_time, end_time)

    #modify_single_office_hour
    def modify_single_office_hour(self, person_id, old_date, old_start_time, old_end_time, new_date, new_start_time, new_end_time):
        # Check if person_id exists and has office hours
        if person_id in self.office_hours and old_date in self.office_hours[person_id]:
            current_office_hours = self.office_hours[person_id][old_date]
            for index, office_hour in enumerate(current_office_hours):
                if office_hour['start_time'] == old_start_time and office_hour['end_time'] == old_end_time:
                    # Modify the office hour to new_date, new_start_time, new_end_time
                    self.office_hours[person_id][old_date][index] = {'start_time': new_start_time, 'end_time': new_end_time}
                    # Remove the old office hour if new date is different
                    if old_date != new_date:
                        self.office_hours[person_id][new_date] = self.office_hours[person_id].get(new_date, [])
                        self.office_hours[person_id][new_date].append({'start_time': new_start_time, 'end_time': new_end_time})
                        del self.office_hours[person_id][old_date][index]
                        if not self.office_hours[person_id][old_date]:
                            del self.office_hours[person_id][old_date]
                    return True  # Successfully modified the office hour
        return False  # Unable to modify the office hour

    #modify_remaining_office_hours
    #
    """
    def modify_remaining_office_hours(modify_single_office_hour(self, person_id, start_date, old_start_time, old_end_time, new_day_of_week, new_start_time, new_end_time))
        date_of_first_office_hours = get_first_day_of_week_after_date(start_date, old_day_of_week)
        for date in get_all_dates(date_of_first_office_hours, self.semester_end_date):
            self.modify_single_office_hour(person_id, date, old_start_time, old_end_time, new_date, new_start_time, new_end_time):
    """
    #modify_office_hours

    #remove_single_office_hour
    def remove_single_office_hour(self, person_id, date, start_time, end_time):
        if person_id in self.office_hours and date in self.office_hours[person_id]:
            current_office_hours = self.office_hours[person_id][date]
            for index, office_hour in enumerate(current_office_hours):
                if office_hour['start_time'] == start_time and office_hour['end_time'] == end_time:
                    del self.office_hours[person_id][date][index]
                    if not self.office_hours[person_id][date]:
                        del self.office_hours[person_id][date]
                    return True  # Successfully removed the office hour
        return False  # Unable to remove the office hour
        
    #remove_remaining_office_hours
    def remove_remaining_office_hours(self, person_id, start_date, day_of_week, start_time, end_time):
        current_date = start_date
        while current_date <= self.semester_end_date:
            if current_date.weekday() == day_of_week:
                self.remove_single_office_hour(person_id, current_date, start_time, end_time)
            current_date += timedelta(days=1)
    #remove_office_hours # self, person_id, date, start_time, end_time, additional=False):
    def remove_office_hours(self, person_id, day_of_week, start_time, end_time):
        self.remove_remaining_office_hours( person_id, self.semester_start, day_of_week, start_time, end_time)
    def pretty_print_office_hours(self):
        for person_id, person_schedule in self.office_hours.items():
            print(person_schedule)
            for date, office_hours in person_schedule.items():
                print(f"\tDate: {date.strftime('%Y-%m-%d')}")
                print("\tOffice Hours:")
                for hour in office_hours:
                    print(f"\t\tStart Time: {hour['start_time']} - End Time: {hour['end_time']}")
        
# Example usage:
semester_start = datetime(2024, 1, 3)
semester_end = datetime(2024, 5, 31)
ta_schedule = {'day_of_week': 'Monday', 'start_time': '09:00 AM', 'end_time': '11:00 AM'}

scheduler = OfficeHoursScheduler(semester_start, semester_end, ta_schedule)

#Assignment Example:
scheduler.add_office_hours('Matt', 'Thursday', '10:00 AM', '11:00 AM')

try:
    scheduler.add_single_office_hour('Max', None, '11:00 AM', '12:00 PM')
    scheduler.add_single_office_hour('Max', None, '11:00 AM', '12:00 PM')
    scheduler.add_single_office_hour('Max', None, '11:00 AM', '12:00 PM')
except:
    print("Classic None")

# try:
#     scheduler.add_single_office_hour('Max', datetime(0, 0, 0), '11:00 AM', '12:00 PM')
#     scheduler.add_single_office_hour('Max', datetime(0, 0, 0), '11:00 AM', '12:00 PM')
#     scheduler.add_single_office_hour('Max', datetime(0, 0, 0), '11:00 AM', '12:00 PM')
# except:
#     print("Classic None")

# scheduler.modify_single_office_hour('Matt', datetime(2024, 1, 4), '10:00 AM', '11:00 AM', datetime(2024, 1, 5), '6:00 PM', '7:00 PM')


print(scheduler.pretty_print_office_hours())
#scheduler.add_office_hour(1, datetime(2024, 1, 10), '09:00 AM', '11:00 AM') #next Wednesday
#scheduler.add_office_hour(1, datetime(2024, 1, 12), '10:00 AM', '12:00 PM') #next Fridat
#scheduler.modify_office_hour(1, datetime(2024, 1, 10), '10:00 AM', '12:00 PM')
#scheduler.remove_office_hour(1, datetime(2024, 1, 10))
#scheduler.remove_remaining_office_hours(1, datetime(2024, 1, 10))
#scheduler.modify_remaining_office_hours(1, datetime(2024, 1, 10), '01:00 PM', '03:00 PM')