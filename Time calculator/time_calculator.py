def add_time(start, duration, *args):

    # convert start time to minutes

    start = start.split()
    print("start input:", start)

    start_time = start[0]
    print("start time:", start_time)

    start_hr = start_time[:-3]
    print("start_hr:", start_hr)

    start_min = start_time[-2:]
    print("start_min:", start_min)

    start_in_mins = int(start_hr) * 60 + int(start_min)
    if start[1] == 'PM':
        start_in_mins = start_in_mins + 60 * 12
    else:
        pass

    print("start minutes from 0 oclock:", start_in_mins)

    # convert duration to minutes

    print("duration input:", duration)

    duration_in_mins = int(duration[:-3]) * 60 + int(duration[-2:])
    print("duration in mins:", duration_in_mins)

    # calculate total time if there is no weekday argument

    total_mins_from_0 = start_in_mins + duration_in_mins
    print("total mins from 0 oclock of start:", total_mins_from_0)
    total_hr_from_0 = total_mins_from_0 // 60
    print("total hrs from 0 oclock of start:", total_hr_from_0)

    mins_ans = f"{((total_mins_from_0 % 1440) % 60):02}"

    # split hours in days if applicable

    ## next day
    if total_hr_from_0 >= 24 and total_hr_from_0 < 48:
      hr_ans_24 = total_hr_from_0 - 24
      day_ans = f"(next day)"

    ## same day
    elif total_hr_from_0 < 24:
      hr_ans_24 = total_hr_from_0
      day_ans = None

    ## X days later
    elif total_hr_from_0 >= 48:
      hr_ans_24 = total_hr_from_0 % 24
      days_from_start = total_hr_from_0 // 24
      day_ans = f"({days_from_start} days later)"

    print("how many days:", day_ans)

    # change hrs from 24 to 12

    if hr_ans_24 == 0:
      hr_ans = "12"
      AMPM_ans = "AM"
    elif hr_ans_24 > 0 and hr_ans_24 < 12:
      hr_ans = hr_ans_24
      AMPM_ans = "AM"
    elif hr_ans_24 == 12:
      hr_ans = hr_ans_24
      AMPM_ans = "PM"
    elif hr_ans_24 > 12:
      hr_ans = hr_ans_24 - 12
      AMPM_ans = "PM"
    print("hour in ans:", hr_ans)
    print("AM or PM:", AMPM_ans)

    # return if no weekday argument

    if len(args) == 0:

      if day_ans is None:
        new_time = f"{hr_ans}:{mins_ans} {AMPM_ans}"
        print("return:", f"{hr_ans}:{mins_ans} {AMPM_ans}")
      else:
        new_time = f"{hr_ans}:{mins_ans} {AMPM_ans} {day_ans}"
        print("return:", f"{hr_ans}:{mins_ans} {AMPM_ans} {day_ans}")

    # return if there is weekday argument

    if len(args) != 0:

      ## convert starting weekday to minutes

      for weekday in args:

          start_weekday_in_mins = 0

          print("weekday input:", weekday)

          if weekday.lower() == "monday":
            pass
          elif weekday.lower() == "tuesday":
            start_weekday_in_mins += 60 * 24
          elif weekday.lower() == "wednesday":
            start_weekday_in_mins += 60 * 24 * 2
          elif weekday.lower() == "thursday":
            start_weekday_in_mins += 60 * 24 * 3
          elif weekday.lower() == "friday":
            start_weekday_in_mins += 60 * 24 * 4
          elif weekday.lower() == "saturday":
            start_weekday_in_mins += 60 * 24 * 5
          elif weekday.lower() == "sunday":
            start_weekday_in_mins += 60 * 24 * 6

          print("start weekday in mins:", start_weekday_in_mins)

          end_weekday = (total_mins_from_0 + start_weekday_in_mins) // 1440
          if (total_mins_from_0 + start_weekday_in_mins < 1440) or (end_weekday % 7 == 0):
            weekday_ans = "Monday"
          elif (end_weekday == 1) or (end_weekday % 7 == 1):
            weekday_ans = "Tuesday"
          elif (end_weekday == 2) or (end_weekday % 7 == 2):
            weekday_ans = "Wednesday"
          elif (end_weekday == 3) or (end_weekday % 7 == 3):
            weekday_ans = "Thursday"
          elif (end_weekday == 4) or (end_weekday % 7 == 4):
            weekday_ans = "Friday"
          elif (end_weekday == 5) or (end_weekday % 7 == 5):
            weekday_ans = "Saturday"
          elif (end_weekday == 6) or (end_weekday % 7 == 6):
            weekday_ans = "Sunday"

          print("ending weekday:", weekday_ans)

      if day_ans is None:
        new_time = f"{hr_ans}:{mins_ans} {AMPM_ans}, {weekday_ans}"
        print("return:", f"{hr_ans}:{mins_ans} {AMPM_ans}, {weekday_ans}")
      else:
        new_time = f"{hr_ans}:{mins_ans} {AMPM_ans}, {weekday_ans} {day_ans}"
        print("return:", f"{hr_ans}:{mins_ans} {AMPM_ans}, {weekday_ans} {day_ans}")

    return new_time
