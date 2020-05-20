import csv
# import os
SalesRegions = {}


try:
    f = open('500000 Sales Records.csv', 'r')
except IOError:
    print("Sorry an error has occurred.")
    exit()

with f:
    reader = csv.reader(f)
    next(f)
    for row in reader:
        SalesRegions[row[0]] = row[1]        # A list of sales regions.
        if row[0] == "Sub-Saharan Africa":
            pass

    print(SalesRegions.keys())
    print(len(SalesRegions.keys()))

# Totals per sales region (repeated for each sales region)
# a- The number of total units sold for the region
# b- The average revenue of all the units sold for the region
# c- The total revenue for the region




