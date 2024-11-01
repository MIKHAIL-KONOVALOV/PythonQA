number = 0
tab = "   "
for i in range(0, 10):
    for j in range(1, 11):
        if number > 9:
            tab = "  "
        number = i * 10 + j
        print(number, tab , end ="")
    print("")
i = 1
j = 1
while i < 10:
    while j < 10:
        print(i * j, end="\t")
        j += 1
    print("\n")
    j = 1
    i += 1