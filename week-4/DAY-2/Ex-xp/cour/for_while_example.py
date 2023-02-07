a_list = ['a', 'a', 'c', 'a', 'c','a', 'a', 'a', 'd', 'a', 'a', 'a', 'e', 'a', 'a', 'a']
        
while 'a' in a_list:
    a_list.remove('a')

print(a_list)



a_list = ['a', 'a', 'c', 'a', 'c','a', 'a', 'a', 'd', 'a', 'a', 'a', 'e', 'a', 'a', 'a']

b_list = []
for char in a_list:
    if char != 'a':
        b_list.append(char)

print(b_list)