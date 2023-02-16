file_location = r"C:\Users\noana\Desktop\sublime-text\DI-exercises-projects\week-5\DAY-4\Ex-cour\list_name.txt"

all_text = ""
text_lines = []

with open(file_location, 'r') as file:
    print(file.tell()) # tell() tells where the pointer is 
    all_text: str = file.read() # ca commence a partir de 0
    print(file.tell())
    file.seek(0) # puts the pointer at a given location (0[zero] means the start)
    print(file.tell())
    text_lines: list = file.readlines()

# read the file line by line

# read only the 5th line of the file
print(text_lines[4])

# read only the 5th first characters of the file
print(all_text[:5])

# read all the file and return it as a list of strings. then split each word
# print(all_text.split("\n")) # split c est linvers de join

# find how many occurences of the names "Darth", "Luke" and "Lea" are in the file
darth = 0
luke = 0
lea = 0
for name in text_lines:
    if name.strip("\n") == "Darth":
        darth += 1

    if name.strip("\n") == "Luke":
        luke += 1

    if name.strip("\n") == "Lea":
        lea += 1


with open(file_location, "a") as file:
    file.write("\nNoa")

for name in enumerate(text_lines):
    if name.strip("\n") == "Luke":
        name = name.strip("\n") + "SkyWalker\n"

print(text_lines)


