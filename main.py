data = (3, 24, 8, 9, True, 8.3,  7, 24)
print(len(data))

for el in data:
    print(el, end = ' ')
print('\n')
new_data = tuple(data)
print(new_data)