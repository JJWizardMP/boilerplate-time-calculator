'''
@File    :   time_calculator.py
@Time    :   2021/11/15 13:00:00
@Author  :   JJwizardMP
@Version :   1.0.1
@License :   GLP v.2
@Desc    :   Solution to FCC Python Project: Time Calculator
'''
def add_time(start, duration, day=None):
    # days week
    daysweek = {
        0: "Sunday", 1: "Monday", 2: "Tuesday",
        3: "Wednesday", 4: "Thursday", 5: "Friday",
        6: "Saturday", "sunday": 0, "monday": 1,
        "tuesday": 2, "wednesday": 3, "thursday": 4,
        "friday": 5, "saturday": 6
    }
    # split hour format
    TIME, pm = start.split()
    HR, MIN = TIME.split(":")
    PM = 12 if(pm == "PM") else 0
    # split add time
    addhr, addmi = duration.split(":")
    # sum minutes
    summin = (int(MIN) + int(addmi))
    mi =  summin % 60
    hc = int(summin / 60)
    # sum hours
    sumhr = (int(HR) + PM + int(addhr) + hc)
    days =  int(sumhr / 24)
    newhr = (sumhr % 24)
    newpm = "PM" if(newhr > 11) else "AM"
    newhr = newhr % 12 if (newhr > 12) else 12 if(newhr == 0) else newhr 
    # calculate days
    if(day):
      keyday = (daysweek[day.lower()] + days) % 7
      newday = daysweek[keyday]
    # Create format
    mi = str(mi) if(mi>9) else "0" + str(mi)
    new_time = str(newhr) + ":" + mi + " " + str(newpm)
    if(day):
        new_time += ", " + newday
    new_time += " (" + str(days) + " days later)" if(days > 1) else " (next day)" if (days == 1) else ""
    return new_time
