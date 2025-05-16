# take 2 numbers as input
num1 = int(input("enter first number: \n"))
num2 = int(input("enter second number: \n"))

# add those numbers
addition = num1 + num2

# subtract those numbers
if num1 > num2:
    subtraction = num1 - num2
else:
    subtraction = num2 - num1

# multiply those numbers
multiplication = num1 * num2

# divide those numbers
if num1 > num2:
    divide = num1 / num2
else:
    divide = num2 / num1

#print output of all of them at once with proper message
print("addition of these numbers is: " + str(addition))
print("subtraction of these numbers is: " + str(subtraction))
print("multiplication of these numbers is: " + str(multiplication))
print("divide of these numbers is: " + str(divide))
