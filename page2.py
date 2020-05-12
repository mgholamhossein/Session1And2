# Session 2
# C = input("Enter C: ")
C = 10

F = (9 / 5) * C + 32
C = (F - 32) / (9 / 5)
print(F, C)

# Exercise 2
car = input("Enter the car type:")
print("selected car is %s" % car)

# Exercise 3
firstName = input("Enter first name :")
lastName = input("Enter last name :")
print("The initial is: " + firstName[0].upper() + "." + lastName[0].upper() + ".")

# Exercise 4
guestnum = int(input("Enter the number:"))
if guestnum >= 8:
    print("wait")
else:
    print("table is ready!")

# Exercise 5
num = int(input("Enter a number:"))
if num % 10 == 0:
    print("num is a multiply of 10")
else:
    print("num is NOT a multiply of 10")

# Exercise 6
num1 = int(input("Enter a number bw 0 and 100"))
if num1 > 100 or num1 < 0:
    print("wrong value")
elif num1 % 10 == 0:
    print("HiFive and HiEven")
elif num1 % 5 == 0:
    print("HiFive")
elif num1 % 2 == 0:
    print("HiEven")
else:
    print("good job")
