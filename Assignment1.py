import csv
import os
import datetime
from turtledemo.penrose import star

regionsname = []
TUnitSold1  = 0
TUnitSold2  = 0
TUnitSold3  = 0
TUnitSold4  = 0
TUnitSold5  = 0
TUnitSold6  = 0
TUnitSold7  = 0
TRevenu1 = TRevenu2 = TRevenu3 = TRevenu4 = TRevenu5 = TRevenu6 = TRevenu7 = 0

if os.path.exists ('500000 Sales Records.csv'):  # check the existence of the csv file using os library
    mydata = open ("100 Sales Records.csv", 'rt')
    reader = csv.DictReader (mydata)
else:
    print ("Sorry an error has occurred.")      # warning if the csv file doesn't exist

next (reader)   # remove the first line

for row in reader:
    if row['Region'] not in regionsname:
        regionsname.append (row['Region'])
    if row['Region'] == 'Central America and the Caribbean':
        TUnitSold1  += int(row['Units Sold'])
        TRevenu1    += float(row['Total Revenue'])
    elif row['Region'] == 'Europe':
        TUnitSold2  += int(row['Units Sold'])
        TRevenu2    += float(row['Total Revenue'])
    elif row['Region'] == 'Sub-Saharan Africa':
        TUnitSold3  += int(row['Units Sold'])
        TRevenu3    += float(row['Total Revenue'])
    elif row['Region'] == 'Australia and Oceania':
        TUnitSold4  += int(row['Units Sold'])
        TRevenu4    += float(row['Total Revenue'])
    elif row['Region'] == 'Asia':
        TUnitSold5  += int(row['Units Sold'])
        TRevenu5    += float(row['Total Revenue'])
    elif row['Region'] == 'Middle East and North Africa':
        TUnitSold6  += int(row['Units Sold'])
        TRevenu6    += float(row['Total Revenue'])
    elif row['Region'] == 'North America':
        TUnitSold7  += int(row['Units Sold'])
        TRevenu7    += float(row['Total Revenue'])

# print(*regionsname, sep = ", ")


TotalUnitSoldList = [TUnitSold1, TUnitSold2, TUnitSold3, TUnitSold4, TUnitSold5, TUnitSold6, TUnitSold7]
TotalRevenueOfSale = [TRevenu1, TRevenu2, TRevenu3, TRevenu4, TRevenu5, TRevenu6, TRevenu7]
AvgRevenuPerUnit = [TRevenu1/TUnitSold1, TRevenu2/TUnitSold2, TRevenu3/TUnitSold3, TRevenu4/TUnitSold4, TRevenu5/TUnitSold5, TRevenu6/TUnitSold6, TRevenu7/TUnitSold7]


print(regionsname[0])

# # a- The number of total units sold for the region
# x = df.groupby (df.Region)[
#     'Units Sold'].sum ()  # Filter data based on Region and calculate the summation of units sold for each group
#
# # c- The total revenue for the region
# y = df.groupby (df.Region)[
#     'Total Revenue'].sum ()  # Filter data based on Region and calculate the summation of Total Revenue for each group
#
# # b- The average revenue of all the units sold for the region
# z = y / x

ReportLine1 = "Sales Report"
ReportLine2 = "------------"
ReportLine3 = "Produced on: " + str (datetime.date.today ())  # Generate the date of report using time library

print (ReportLine1.center (150, ' ') + "\n" + ReportLine2.center (150, ' ') + "\n")
print ((ReportLine3.center (150, ' ')) + "\n")
print ("Regions analysed: ", end='')
print (*regionsname, sep=", ")
print ("\nTotal, %d regions." % len (regionsname) + "\n")

for i in range(len(regionsname)):
    print (regionsname[i] + "\n")
    print ("\tTotal units sold:            %d" % (TotalUnitSoldList[i]))
    print ("\tAverage revenue per unit:    $%.2f" % (AvgRevenuPerUnit[i]))
    print ("\tTotal revenue of sales:      $%.2f" % (TotalRevenueOfSale[i]) + "\n")

print ("Grand Totals\n")
print ("\tTotal units sold:            %d" % (sum(TotalUnitSoldList)))
print ("\tAverage revenue per unit:    $%.2f" % (sum(AvgRevenuPerUnit) / len (AvgRevenuPerUnit)))
print ("\tTotal revenue of sales:      $%.2f" % (sum(TotalRevenueOfSale)))
