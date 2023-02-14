from datetime import datetime, date
import random
import string

print(random.randint(1, 10))

print(string.ascii_uppercase)

now_time = datetime.now()

print(now_time)
print(now_time.hour)
print(now_time.minute)
print(now_time.second)
print(now_time.date())

now_date = date.today()
print(now_date)
