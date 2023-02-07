
#CHALLENGE 2 

# Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.

# user's word : "ppoeemm" ➞ "poem"
# user's word : "wiiiinnnnd" ➞ "wind"
# user's word : "ttiiitllleeee" ➞ "title"
# user's word : "cccccaaarrrbbonnnnn" ➞ "carbon"

in_str = "cccccaaarrrbbonnnnn"

result_str = in_str[0] #0 c est la place du premier c 

for char in in_str[1:]:
    if result_str[-1] != char:
        result_str += char

        print(result_str)

