data = set('helllllo')
print(data)
data1 = {5, 7, 3, 2, 2, 7, 1}
print(data1)

data1.add(26)
data1.update(['ok', True, (45, '567', False), 11, (45, '567', False)])
print(data1)
data1.remove("ok")
print(data1)
data1.pop()
print(data1)
# Deleting by pop in tuple
tup = [34, 'wer', 34, 345, 79]
print(tup)
tup.pop()
print(tup)
# В словаре pop() удаляет первый а в списке последний элемент!!!!


# frozenSet кортеж + множество
var1 = frozenset((3,45,96,'11','11'))
for el in var1:
    print(el)
