# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will
# turn 100 years old.
name = input("What is your name?")
print ("Hello " + name)
number = int(input("Age?"))
print("You will be 100 in the year " + str(2017 - number + 100))
