ifile_location1 = 'files/file1.txt'

# mode 'w' - write into file
with open(file_location1, 'w') as file:
    file.write("This is text from python!")

lines = ['The first line\n', 'The second line\n', 'The third line\n']

file_location2 = 'files/file2.txt'

with open(file_location2, 'w') as file:
    file.writelines(lines)

