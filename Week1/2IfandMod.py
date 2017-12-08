num = int(input("Give me a number"))
if (num % 4) == 0:
    print("You gave me an even number divisible by 4")
elif (num % 2) == 0:
    print ("You gave me an even number")
else:
    print("You gave me an odd number")

(num, check) = int(input("num?")), int(input("check"))
if (num % check) == 0:
    div = str(int(num/check))
    print ("num is a multiple of check and the result is: " + div)
else:
    print("ggwp")
