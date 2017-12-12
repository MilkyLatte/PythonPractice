xs = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
bs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
ys = []
for x in xs:
    if x in bs:
        ys.append(x)
print(ys + [1234567])
