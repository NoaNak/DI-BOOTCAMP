# 1-if, initial condition
# 2-elif, what to check if the previous 'if' wan't true
# 3-else, what happends when everything returns False
apple_color: str = input("Apple color: ")
apples_inside_basket: int = int(input("Apples inside basket: "))

if apple_color != 'green':
    print("Not green")
elif apples_inside_basket > 6:
    print("Higher than 6")
else:
    print("All of the previous conditions are False")