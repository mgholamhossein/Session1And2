# Session 3 (21 April 2020)
# Exercise 1
num = input("enter a number \n")

while num != 'q' and num != 'Q':
    number = int(num)
    if number % 10 == 0:
        print("it is multiple of 10")
    else:
        print("it's not")

    num = input("enter a number \n")

# Exercise 2
# Using for and continue or break, print a list of even numbers from 1 to 100
for numbers in range(1, 101):
    if numbers % 2 == 0:
        print(numbers)

# Exercise 3
# Modify exercise 2 to prompt the user to provide a number, then determine that the number is even or odd.
# The program needs to ask the user if he want to continue or not, if yes, then the program asks for another number, if No, then the program ends.
while True:
    input3 = input("enter a number")
    if int(input3) % 2 == 0:
        print("EVEN number")
    else:
        print("ODD number")

    input3 = input("want to continue?")
    if input3.upper() == 'YES':
        continue
    elif input3.upper() == 'NO':
        break

# Exercise 4
# Write a program that choose an integer between 0 and 100, inclusive. The program prompts the user
# to enter a number continuously until the number matches the chosen number. For each user input,
# the program tells the user whether the input is too low or too high, so the user can choose the next
# input intelligently.
# After the user guess correctly, the program will print: “Bravo you guess correctly after … times”.
import random

ComputerNum = random.randrange(1, 101)
print(ComputerNum)
counter = 0
while True:
    input4 = int(input("Enter a number"))
    counter += 1
    if input4 == ComputerNum:
        print("Bravo you guess correctly after %d times" % counter)
        break
    elif input4 < ComputerNum:
        print("The input is too low")
    else:
        print("The input is too high")

# Exercise 5
# 1. Add two colours to the end, 'black' and 'white'.
# 2. Change the third item to 'yellow'.
# 3. Delete the colour green by position.
# 4. Delete the colour red by name.
# 5. Make a for loop to print each remaining item, capitalized, with a line number in front of it.
mylist = ['red', 'green', 'blue']
print(mylist)
mylist = mylist + ['black', 'white']
print(mylist)
mylist[-3] = 'yellow'  # or mylist[2] = 'yellow'
print(mylist)
del mylist[1]
print(mylist)
mylist.remove('red')
print(mylist)
lenght = len(mylist)
for x in range(0, lenght):
    print(x + 1, mylist[x].capitalize())
# another way:
# i = 1
# for a in mylist:
#   print (str(i) + " " + a.capitalize())
#   i+=1


# Exercise 6
# Create a list of 20 numbers, randomly assigned.
# To generate the list, we can use:
# random_list = [random.randrange(1, 100) for i in range(20)]
# 1. Scan the list and display several values using a manual method:
# 1. The minimum, the maximum, the count and the average.
import random

List1 = []
for x in range(0, 20):
    List1.append(random.randrange(1, 101))
print(List1)
lenght = len(List1)
counter = 0
minval = List1[0]


def findMax(x):
    maxval = x[0];
    for a in x:
        if (a > maxval):
            maxval = a
    return maxval


def findMin(x):
    minval = x[0];
    for a in x:
        if (a < minval):
            minval = a
    return minval


def findSum(x):
    sum = 0
    for a in x:
        sum = sum + a
    return sum


def findCount(x):
    count1 = 0;
    for a in x:
        count1 = count1 + 1
    return count1


def findAvg(x):
    sums = findSum(x)
    counts = findCount(x)
    avg = sums / counts
    return avg


print(findMax(List1))
print(findMin(List1))
print(findSum(List1))
print(findCount(List1))
print(findAvg(List1))

# Exercise 7
# Repeat Exercise 6 using built in functions
print("max is %d" % max(List1))
print("min is %d" % min(List1))
print("count is %d" % len(List1))
print("avg is %d" % (sum(List1) / len(List1)))

# Exercise 8
# repeat exercise 7 using below list
my_list = ['A', 'B', 1, 2, 3]
print(my_list)
print("max is %d" % max(my_list))
print("min is %d" % min(my_list))
print("count is %d" % len(my_list))
print("avg is %d" % (sum(my_list) / len(my_list)))
