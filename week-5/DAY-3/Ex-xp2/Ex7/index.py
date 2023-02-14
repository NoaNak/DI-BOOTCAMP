import datetime

def upcoming_holiday():
    now = datetime.datetime.now()
    holidays = {
        "New Year's Day": datetime.datetime(now.year, 1, 1),
        "Independence Day": datetime.datetime(now.year, 7, 4),
        "Thanksgiving": datetime.datetime(now.year, 11, 1) + datetime.timedelta( (3- datetime.datetime(now.year, 11, 1).weekday()) % 7 ),
        "Christmas Day": datetime.datetime(now.year, 12, 25),
    }
    today = datetime.date.today()
    print(f"Today's date is {today.strftime('%A, %B %d, %Y')}")
    next_holiday, holiday_date = min(holidays.items(), key=lambda x: abs(x[1] - now))
    time_left = holiday_date - now
    print(f"The next upcoming holiday is {next_holiday}, which is in {time_left.days} days and {time_left.seconds // 3600} hours.")

upcoming_holiday