import random

def get_random_temp():
    temp = random.randint(-10, 40)
    return(temp)

# get_random_temp()

def main():
    temp = get_random_temp()
    print(f"The temperature right now is {temp} degrees Celsius.")

    if temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today")
    
    elif temp > 0 and temp < 16:
        print("Quite chilly! Don’t forget your coat !")

    elif temp > 16 and temp < 23:
        print("I love this temperature !")

    elif temp > 24 and temp < 32:
        print("We can go to tan !")

    else:
        print("To hot outside !!!")

main()

# def get_random_temp(season):
#     if season == "hiver":
#         temp = random.randint(-10, 16)
#     # return(temp)

# # import random

# def main():
#     input("please choice a season: ")

# get_random_temp("season")

