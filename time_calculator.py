def add_time(start, duration, day = None):

    #Our storage
    hour_minute_day = []
    hour_minute_day.insert(0, start[-2:])
    hour_minute_day.insert(0, start[-5:-2])
    hour_minute_day.insert(0, start[:-6])
    hour_minute_day.insert(3, duration[:-3])
    hour_minute_day.insert(4, duration[-2:])
    day_period_changed = 0

    #Convert hours and minutes to int
    hour_minute_day[0] = int(hour_minute_day[0])
    hour_minute_day[1] = int(hour_minute_day[1])
    hour_minute_day[3] = int(hour_minute_day[3])
    hour_minute_day[4] = int(hour_minute_day[4])

    #Adding part to each other
    hour_minute_day[1] = hour_minute_day[1] + hour_minute_day[4]
    if hour_minute_day[1] >= 60:
        hour_minute_day[3] = hour_minute_day[3] + hour_minute_day[1]//60
        hour_minute_day[1] = hour_minute_day[1] % 60
    

    day_period_changed += hour_minute_day[3]//12
    hour_minute_day[0] = hour_minute_day[0] + hour_minute_day[3] % 12 
        
    #Mod hour part
    if hour_minute_day[0] >= 12:
        day_period_changed += 1                
        if hour_minute_day[0] > 12:
            hour_minute_day[0] = hour_minute_day[0] % 12

    #If we need to change AM - PM
    if day_period_changed % 2 == 1:
        if hour_minute_day[2] == 'AM': hour_minute_day[2] = 'PM'
        else: 
            hour_minute_day[2] = 'AM'
            day_period_changed += 1

    #Changing day_period_changed's use before this line it was using change in am pm but after this it keeps the day count
    day_period_changed = day_period_changed // 2

    #If a minutes length 0 then we put a 0 to its start like 12:5 -> 12:05
    if len(str(hour_minute_day[1])) == 1: hour_minute_day[1] = '0' + str(hour_minute_day[1])

    #Things we do if we receive a day of week(optional)
    if day != None:
        hour_minute_day.insert(5, day.lower())
        day = day.capitalize()
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        a = days.index(day)
        day = days[a-7+day_period_changed%7]
        if day_period_changed == 1:
            strin = """{}:{} {}, {} (next day)""".format(hour_minute_day[0], hour_minute_day[1], hour_minute_day[2], day)
            return strin
        elif day_period_changed == 0:
            strin = """{}:{} {}, {}""".format(hour_minute_day[0], hour_minute_day[1], hour_minute_day[2], day)
            return strin           
        else:
            strin = """{}:{} {}, {} ({} days later)""".format(hour_minute_day[0], hour_minute_day[1], hour_minute_day[2], day, day_period_changed)
            return strin
    
    #Returns if day is None
    if day_period_changed == 1:
        strin = """{}:{} {} (next day)""".format(hour_minute_day[0], hour_minute_day[1], hour_minute_day[2])
        return strin
    elif day_period_changed == 0:
        strin = """{}:{} {}""".format(hour_minute_day[0], hour_minute_day[1], hour_minute_day[2])
        return strin
    else:
        strin = """{}:{} {} ({} days later)""".format(hour_minute_day[0], hour_minute_day[1], hour_minute_day[2], day_period_changed)
        return strin
