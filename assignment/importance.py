from datetime import datetime as d


# Minimum importance - 5,  Maximum importance 1

# The importance scale goes as follows
# 1 - Due yesterday, Due tomorrow
# 2 - Estimated time is greater than 30 minutes a day
# 3 - Estimated time is between 20 - 30 minutes a day
# 4 - Estimated time is between 15 - 20 minutes a day
# 5 - Estimated time is lower than 15 minutes a day


# Return (importance, daily time amount)
def importance_calc(due_date, time_estimate):
    today = d.now().date()
    if due_date <= today:
        print(0)
        return 1, time_estimate
    else:
        day_difference = due_date - today
        day_difference = day_difference.days
        time_per_day = time_estimate/day_difference
        print(time_per_day)
        if day_difference <= 1:
            return 1, time_per_day
        elif time_per_day >= 30:
            return 2, time_per_day
        elif 20 <= time_per_day < 30:
            return 3, time_per_day
        elif 15 <= time_per_day < 20:
            return 4, time_per_day
        elif time_per_day < 15:
            return 5, time_per_day
