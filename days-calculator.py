days = int(input("day"))
month = int(input("month"))
year = int(input("year"))
added_days = int(input("added days"))

def cal(days, month, year, added_days):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# every 4 year february becomes 29 day
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        days_in_month[1] = 29
# conditions
    if not (1 <= month <= 12):
        raise ValueError("Invalid month. Month must be between 1 and 12.")

    if not (1900 <= year <= 2026):
        raise ValueError("Invalid year. Year must be between 1900 and 2026.")

    if added_days > 1000:
        raise ValueError("Maximum allowed added days is 1000.")
# when we add days
    if added_days > 0 :
        while days > days_in_month[month - 1]:
            days -= days_in_month[month - 1]
            month += 1
        if month > 12:
            month = 1
            year += 1
    else:
        days = days + added_days
        while days < 0:
            days = days_in_month[month - 2] + days
            month -= 1
        if month < 1:
            month += 12
            year -= 1



    return days, month, year

print (cal(days, month , year, added_days))