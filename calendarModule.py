import calendar

month, day, year = map(int, input().split())

if 2000 < year < 3000:
    # Get the day of the week (0 = Monday, 1 = Tuesday, ..., 6 = Sunday)
    week_number = calendar.weekday(year, month, day)

    days = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']

    print(days[week_number])

# import calendar
# print(calendar.TextCalendar(firstweekday=5).formatyear(2024))