# Session 1
first = "jane"
last = "Doe"
salary = 20080.45
symbol = "#"
repeat = 15
age = 25
res1 = "welcome \"" + first + last + "\""

print(res1)
print("The salary is %.2f" %salary)
print("the symbol %s repeated %d is " %(symbol,repeat) + symbol *repeat)

months = age * 12
days = age * 365

print("months %d, days %d"%(months,days))

# Homework
firstName = input("Enter first name :")
lastName = input("Enter last name :")
print("The initial is: " + firstName[0].upper() + "." + lastName[0].upper()+ "." )