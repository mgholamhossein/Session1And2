# Session5 5 May 2020
# Exercise 1
#  How many order records are from Europe?
#  What is the total amount of units sold?
#  Provide a list of "Item Types" without duplicates (hint, you can use a dictionary for this).
import csv

f = open("100 Sales Records.csv", 'rt')
reader = csv.reader(f)
count = 0
soldnum = 0
next(f)
itemType = {}
for row in reader:
    if row[0] == "Europe":
        count = count + 1
    soldnum += int(row[8])

    # row[2]
    # [row[0], int(row[1])]
    itemType[row[2]] = row[3]
print("order records from Europe is:", count)

print("total sold is", soldnum)

list = itemType.keys()
print(list)
f.close()

# Exercise 2
# Copy only three columns
#  Rigon
#  Country
#  total profit
#  from 100 Sales Records.csv to a new file data.csv
import csv

f = open("100 Sales Records.csv", 'rt')

reader = csv.reader(f)

csv_data = []
for row in reader:
     list = []
     list.append(row[0])
     list.append(row[1])
     list.append(row[13])
     csv_data.append(list)
f.close()

with open('data.csv', 'w', newline="") as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(csv_data)



