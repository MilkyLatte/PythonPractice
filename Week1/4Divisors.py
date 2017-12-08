n = int(input("Give me a number "))
xs = range(1, n)
dvs = []
for x in xs:
    if (n % x) == 0:
        dvs.append(x)
print(dvs)
