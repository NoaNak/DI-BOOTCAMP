# While loop is based on a condition


number = 0

while number < 10:
    print("HOLLA")
    number += 1

# Break 
while True:

    print("LOOPING")

    if number == 11:
        print("BREAKING LOOP")
        break
    
    elif number > 5:
        print("CONTINUING LOOP")
        number += 1
        continue

    print("SOMETHING ELSE")
    
print("OUTSIDE WHILE LOOP")

