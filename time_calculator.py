'''
@File    :   time_calculator.py
@Time    :   2023/10/16 08:00:00
@Author  :   JJwizardMP
@Version :   1.0.2
@License :   GLP v.2
@Desc    :   Solution to FCC Python Project: Time Calculator
'''


def add_time(start, duration, day=None):
  # Define a dictionary to map days of the week to numbers
  daysweek = {
      "sunday": 0,
      "monday": 1,
      "tuesday": 2,
      "wednesday": 3,
      "thursday": 4,
      "friday": 5,
      "saturday": 6
  }
  day_str = ""
  # Split the input start time and duration
  time, pm = start.split()
  hr, minutes = map(int, time.split(":"))
  add_hr, add_min = map(int, duration.split(":"))

  # Calculate the total minutes and hours
  total_min = 60 * (hr + add_hr) + minutes + add_min
  total_hr, new_min = divmod(total_min, 60)
  total_hr += 12 if pm == "PM" else 0

  # Calculate the new time and days
  days_later, new_hr = divmod(total_hr, 24)
  new_pm = "PM" if new_hr >= 12 else "AM"
  new_hr = new_hr % 12 or 12

  # Calculate the new day if a day is specified
  if day:
    start_day = daysweek[day.lower()]
    new_day_index = (start_day + days_later) % 7
    new_day = [
        key for key, value in daysweek.items() if value == new_day_index
    ][0]
    day_str = f", {new_day.capitalize()}"

  # Determine the days later string
  days_later_str = " (next day)" if days_later == 1 else f" ({days_later} days later)" if days_later > 1 else ""

  # Format the new time as a string
  new_time = f"{new_hr}:{str(new_min).zfill(2)} {new_pm}{day_str}{days_later_str}"

  return new_time
