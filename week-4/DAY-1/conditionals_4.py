apple_color = 'green'
apples_inside_basket = 5

# and - both conditions must be True
if apple_color == 'green' and apples_inside_basket < 6:
    print("BOTH CONDITIONS ARE TRUE")
else:
    print("At least one condition isn't TRUE")

# or - at least one condition must be True
if apple_color == 'red' or apples_inside_basket < 6:
    print("At least one condition IS TRUE")
else:
    print("ALL OF THE CONDITONS ARE FALSE")