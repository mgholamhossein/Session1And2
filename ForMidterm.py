my_dict = {'us': 'USA', 'fr': 'France', 'uk': 'Eng'}

for key, value in my_dict.items ():
    print (key, value)

for key in my_dict:
    print (key, my_dict[key])

my_dict.keys ()
my_dict.items ()

print ('uu' in my_dict)

with open ("Midterm.txt") as f:
    for l1 in f: # printing line by line
        print(l1.rstrip())

# with open ("Midterm.txt") as f:
#     l2 = f.readlines() # Creating a List from a File
#     print(l2)

with open ("Midterm1.txt",'w+') as f:
    print(f.readable())
    print(f.writable())
    f.write("hello")
    f.seek(0)
    print(f.read())
