# Creating 
a_list = []
a_list = ['a', 'b', 1, 2, [1,2, ['surpirse']]]

# Indexing - get the 'surprise' string
print(a_list[4][2][0])

numbers = [10, 'a', 20, 'b', 30, 'c', 40, 50]
# take items from 20 until 30
print(numbers[2:5])
# negative indexing 
print(numbers[-4: -2])
# LIST [start : end : step]
numbers = [1,2,3,4,5,6,7,8,9,10]
# Get all even numbers
print(numbers[1::2])


# Updating - change second item 'b' to 100
a_list[1] = 100
print(a_list)

# Adding

# To add to the end of the list - use .append
a_list: list = []
a_list.append(1)
a_list.append(2)
a_list.append(3)
a_list.append(5)

# Insert number 4 between 3 and 5
a_list.insert(3, 4)

# Deleting

# .pop - removes an item and returns it. by default uses the last index
item_removed = a_list.pop()
print(item_removed)

# .remove - removes the first occurence of a specific item
b_list = [1,2, 'word', 'word', 3, 4]
b_list.remove('word')
print(b_list)

# del - removes by the index, doesn't return anything
del b_list[0]
print(b_list)

# To remove everything
b_list.clear()

# SORTING
# .sort sorts all items inside list
b_list.sort()

# If we want to preserve the original list - we use sorted
numbers = [6,5,3,2,8,2,1,8,4,2,4]
numbers_sorted = sorted(numbers)
print(numbers_sorted)

