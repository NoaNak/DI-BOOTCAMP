import random
import string

random_string = ''.join(random.choices(string.ascii_letters + string.digits, k = 5))
print(random_string)
