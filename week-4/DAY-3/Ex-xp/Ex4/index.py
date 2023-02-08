users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
numbers = list(range(len(users)))
print(numbers)
link = dict(zip(users, numbers))
print(link)

link2 = dict(zip(numbers, users))
print(link2)

link3 = dict(zip(sorted(users), numbers))
print(link3)