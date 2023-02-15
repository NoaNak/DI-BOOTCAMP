file_location2 = 'files/file2.txt'

text_lines = []

with open(file_location2, 'r') as file:
    text_lines = file.readlines()

# change the forth line - separate into 'The forth line\n' and 'The fifth line\n'
problematic_line: str = text_lines[3]

# "The forth lineThe fifth line"
start_second_line_index = problematic_line.index('T', 2)

forth_line: str = problematic_line[:start_second_line_index]
fifth_line: str = problematic_line[start_second_line_index:]

text_lines[3] = forth_line + '\n'
text_lines.insert(4, fifth_line)
text_lines[-1] += '\n'

print(text_lines)

with open(file_location2, 'w') as file:
    file.writelines(text_lines)
