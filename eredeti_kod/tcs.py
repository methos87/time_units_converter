"""
Time Unit Converter
Created by: Akos Novak
Date: 2023.05.18
Version: 1.2
"""

def myfunction(seconds):
    tl = []
    # print(f"seconds: {seconds}")
    if seconds != 0:
        # Seconds
        seconds_left = seconds % 60
        # print(f"seconds_left: {seconds_left}")
        if seconds_left > 1:
            seconds_s = str(seconds_left) + " seconds"
            tl.append(seconds_s)
        elif seconds_left == 1:
            seconds_s = str(seconds_left) + " second"
            tl.append(seconds_s)
        # Minutes
        minutes = seconds // 60
        minutes_left = minutes % 60
        # print(f"minutes: {minutes}")
        # print(f"minutes_left: {minutes_left}")
        if minutes_left == 1:
            minutes_s = str(minutes_left) + " minute"
            tl.append(minutes_s)
        elif minutes_left > 1:
            minutes_s = str(minutes_left) + " minutes"
            tl.append(minutes_s)
        # Hours
        hours = (minutes// 60)
        hours_left = hours % 24
        # print(f"hours: {hours}")
        # print(f"hours_left: {hours_left}")
        if hours_left == 1:
            hours_s = str(hours_left) + " hour"
            tl.append(hours_s)
        elif hours_left > 1:
            hours_s = str(hours_left) + " hours"
            tl.append(hours_s)
        # Days
        days = hours // 24
        days_left = days % 365
        # print(f"days: {days}")
        # print(f"days_left: {days_left}")
        if days_left == 1:
            days_s = str(days_left) + " day"
            tl.append(days_s)
        elif days_left > 1:
            days_s = str(days_left) + " days"
            tl.append(days_s)
        # Years
        years = days // 365
        years_left = years % 365
        # print(f"years_t: {years}")
        # print(f"years_left: {years_left}")
        if years_left == 1:
            years_s = str(years_left) + " year"
            tl.append(years_s)
        elif years_left > 1:
            years_s = str(years_left) + " years"
            tl.append(years_s)
        tl = tl[::-1]
        te = []
        for i in range(0, len(tl)):
            if i == len(tl)-2:
                te.append(tl[i] + " and ")
            elif i == len(tl)-1:
                te.append(tl[i])
            else:
                te.append(tl[i] + ", ")
        # print(tl)
        # print(te)
        text = "".join(te)
        return text
    else:
        return "now"
    
# Felhasznaló input
input = input()
t = myfunction(int(input))
print(t)