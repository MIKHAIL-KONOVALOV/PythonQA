number = 0
tab = "   "
file = open('Data\\text.txt', 'w')
for i in range(0, 10):
    for j in range(1, 11):
        if number > 9:
            tab = "  "
        number = i * 10 + j
        print(number, tab , end ="")
    print("")
i = 1
j = 1
