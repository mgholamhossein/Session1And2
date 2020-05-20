# Session7 19 May 2020
# Exercise 1
from unittest import result


def my_max(n1=0, n2=0, n3=0):
    if (n1 >= n2 and n1 >= n3):
        maxnum = n1
    elif (n2 >= n1 and n2 >= n3):
        maxnum = n2
    else:
        maxnum = n3
    print (maxnum)


my_max (7, 2)


# Exercise 2
#  Write a function that get a number as its parameter and then return true if the number is divisible by
# 3 otherwise it will return false.
#  Prompt a number from the user and print if the number is divisible by 3 or not by using your function.
def IsdivisableBy3(number):
    if number % 3 == 0:
        return True
    else:
        return False


num1 = int (input ("Provide a number: "))
if (IsdivisableBy3 (num1)):
    print ("%i is divisable by 3" % (num1))
else:
    print ("%i is NOT divisable by 3" % (num1))


# Exercise 3
# Create a function that adds two numbers and returns the value, use it in a sample code scenario.
def addFunc(n1=0, n2=0):
    return (n1 + n2)


num1 = int (input ("Provide a number: "))
num2 = int (input ("Provide a number: "))
print ("the sum of %d and %d is %d" % (num1, num2, addFunc (num1, num2)))


# Exercise 4
# 1. Create a function that takes in a list. The function should print the list items one over the other.
# 2. Modify the previous function to get a title, and use the supplied title as the title of your list.
def TakeList(t='the list', l1=''):
    print (t + ":")
    for i in l1:
        print (i)


mytitle = input ("enter a title for the list")
mylist = list (input ("enter a list"))

TakeList (mytitle, mylist)


# Exercise 5
# Make a function that takes UP TO 3 arguments and returns a list of 1, 2 or 3 items (an array).
def makeList(n1="", n2="", n3=""):
    l1 = list ();
    if (n1 != ""):
        l1.append (n1)
    if (n2 != ""):
        l1.append (n2)
    if (n3 != ""):
        l1.append (n3)
    return l1


print (makeList (1, "hi"))


# Homework
#  Make a function that will print out a row of asterisks depending on the value given to it.
#  Use this in a loop – so we can print a triangle of stars.
def printStarTriangle(num=1):
    i = 0
    while (i <= num):
        print ("*" * i)
        i += 1

printStarTriangle (6)
