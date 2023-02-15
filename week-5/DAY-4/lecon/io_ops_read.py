file_location1 = 'files/file1.txt'

file_text = ""
# mode 'r' - read
with open(file_location1, 'r') as f:
    file_text = f.read()

print(file_text)

file_location2 = 'files/file2.txt'

file_text_lines = []

with open(file_location2, 'r') as f:
    file_text_lines = f.readlines()

print(file_text_lines)

