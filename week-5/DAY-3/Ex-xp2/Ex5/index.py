from datetime import datetime

def time_until_january_1st():
    now = datetime.now()
    year = now.year + 1
    january_1st = datetime(year, 1, 1)
    time_left = january_1st - now
    print("Time left until January 1st:", time_left)

time_until_january_1st()