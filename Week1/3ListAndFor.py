n = int(input("Number?"))
xs = [2, 3, 7, 9, 5, 6, 10, 13, 1, 4]
xs.append(4)
mult5s = []
for x in xs:
    if x < n:
        mult5s.append(x)
print(mult5s)
