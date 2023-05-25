
from datetime import datetime
import pytz
import calendar


def calculate_time_until_next_birthday(birthdate, unit):
    try:
        # Get the current date and time in the "eu-west-1" time zone
        current_date = datetime.now(pytz.timezone('Europe/Dublin')).date()

        # Get the birthdate as a date object
        birthdate_obj = datetime.strptime(birthdate, '%Y-%m-%d').date()

        # Calculate the next birthday year
        next_birthday_year = current_date.year
        if (current_date.month, current_date.day) > (birthdate_obj.month, birthdate_obj.day):
            next_birthday_year += 1

        # Find the next leap year from the current date
        while not calendar.isleap(next_birthday_year):
            next_birthday_year += 1

        # Calculate the next birthday date
        next_birthday = birthdate_obj.replace(year=next_birthday_year)

        # Calculate the time difference until the next birthday
        time_left = next_birthday - current_date

        # Convert the time difference to the specified unit
        if unit == 'hour':
            time_left = int(time_left.total_seconds() / 3600)
        elif unit == 'month':
            time_left = calculate_month_difference(next_birthday, current_date)
        elif unit == 'week':
            time_left = int(time_left.days / 7)
        elif unit == 'day':
            time_left = time_left.days

        return f"{time_left} {unit}s"
    except ValueError:
        raise ValueError("Invalid date provided.")

def calculate_month_difference(date1, date2):
    return (date1.year - date2.year) * 12 + (date1.month - date2.month)

# Example usage
# birthdate = '2000-02-29'
# unit = 'month'
# try:
#     time_left = calculate_time_until_next_birthday(birthdate, unit)
#     print("Time left until next birthday:", time_left, unit)
# except ValueError as e:
#     print("Error:", str(e))
