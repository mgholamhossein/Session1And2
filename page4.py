# Session 4 (28 April 2020)
# Exercise 1
# Create a new list with the first ten values of 2^^n
Mylist1 = []
for a in range (0, 10):
    Mylist1.append (pow (2, a))
print (Mylist1)

powers = [pow (2, a) for a in range (0, 10)]
print (powers)

# Exercise 2
# Create a new list "copied_list_1" by copying the list by assignment (a = b).
mylist = ["A", "B", "C"]
Copied_mylist_1 = mylist
Copied_mylist_2 = mylist.copy ()
mylist[1] = "X"

print ("assign:      ", Copied_mylist_1)
print ("proper copy: ", Copied_mylist_2)

# Exercise 3
# Using a starter PY file, convert a price from USD to CAD and display the result in a readable way. You
# must get all the information from the provided dictionary files. The price and source currency is
# listed on top of the file.
# 1. Open the file "exercise_dictionary.py"
# 2. Look up the currency code exchange rate.
# 3. Look up the currency code name.
# 4. Print the original and converted prices along with the item name (see output next slide
# the CODE is in test.py file


# Exercise 4
#  Create a text file with few line of text
#  Read a multi-line file in as a list.
#  Set a breakpoint to see the effect of the assignment of the file lines to the list.
#  Observe in the debugger screen to see the list formation.

mylist2 = mytest1 = mytest2 = mytest3 = []
with open ('test.txt', 'a+') as myfile:
    print ("Is the file readable? ", myfile.readable ())
    print ("Is the file writable? ", myfile.writable ())
    print ("Is the file seekable? ", myfile.seekable ())
    myfile.write ("bye\n")
    myfile.write ("From python\n")

with open ('test.txt') as myfile:
    mytest3 = myfile.readlines ()
    print ('mytest3', mytest3)

    mylist2 = myfile.readline (2)  # reads two bytes of a line
    myfile.seek (0)
    mytest1 = myfile.readlines (2)
    print ('mylist2', mylist2)
    print ('mytest1', mytest1)
    myfile.seek (0)
    mytest1 = myfile.readlines (6)
    print ('mytest1', mytest1)

    myfile.seek (0)
    mytest2 = myfile.read (13)
    print ('mytest2', mytest2)

    for line in mylist2:
        print (line.rstrip ())
        # for line in myfile:
        #     mylist2.append(line.rstrip())
        # print(mylist2)

# using SEEK with WRITE
f = open ("test_file2.txt", "w+")
f.write ("Testing 123")
f.seek (0)
print (f.read ())
f.seek (4)
f.write ("*")
f.seek (0)
print (f.read ())
f.close ()

# Exercise 5
# Write a program that logs to a file
# The logging should be done by a message and the severioty (E. W. I) (Error, Warning, Informational)
# The logging should display a timestamp on each log
# Write a mock program, and log 3 things(start of program, end of program) and a warning in between.

# To make the program not finish instantly, we can issue "sleep" command in it. like "time.sleep()" to remember to import "time"
# Time.time() gives tou the time in millisecond
import datetime

mytime = datetime.datetime.now ()
print (datetime.datetime.now ())
file5 = open ("test_file_ex5.txt", "w+")
file5.write ("start of the program at ")
file5.write ('{}'.format (mytime))
file5.close ()

import time

with open ("file6_ex5.txt", "w+") as file6:
    file6.write ("program started at: ")
    file6.write (time.asctime (time.localtime (time.time ())))
    file6.write ("\n")
    time.sleep (5)
    file6.write ("WARNING WARNING at: ")
    file6.write (time.asctime (time.localtime (time.time ())))
    file6.write ("\n")
    time.sleep (5)
    file6.write ("program ended at: ")
    file6.write (time.asctime (time.localtime (time.time ())))
    file6.write ("\n")

# My experiments :D
myDict = {'a': 'b', 'x': 'y'}
print ("x" in myDict)

# Exercise 6
import os

if os.path.exists ('test/file6_ex5.txt'):
    print ("True")
    cond = False
    with open ("test/file6_ex5.txt", 'r+b') as file6:
        try:
            print ('success')
            cond = False
        except cond:
            print ("error")
else:
    print ("False")

fname = input ("enter \n")
try:
    f = open (fname, 'r+b')
except IOError:
    print ("coudn't read", fname)
    SystemExit ()
