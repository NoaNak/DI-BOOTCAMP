import random 
random_number = random.randint(1, 100)

def accept_num(num):
    if random_number == num:
        print("Success !")
    else:
        print("Try again")
        
    print(random_number)
    print(num)

accept_num(34)
