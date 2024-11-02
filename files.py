file = open('Data\\text.txt', 'w')

file.write('hello')
file.write('!!!')

file.close()

my_file = open('Data\\text.txt', 'r', encoding='utf-8')
for line in my_file:
    print(line, end='')

print('Ok!')