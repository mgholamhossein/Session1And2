import csv
import os
import datetime

regionsname = []    # the list contains the name of the regions for the report
TUnitSold1 = TUnitSold2 = TUnitSold3 = TUnitSold4 = TUnitSold5 = TUnitSold6 = TUnitSold7 = 0 #total unit solds for each regions
TRevenu1 = TRevenu2 = TRevenu3 = TRevenu4 = TRevenu5 = TRevenu6 = TRevenu7 = 0 # total revenue for each regions

if os.path.exists ('500000 Sales Records.csv'):  # check the existence of the csv file using os library
    mydata = open ("500000 Sales Records.csv", 'r')
    reader = csv.DictReader(mydata) # read the csv file into a dictionary
else:
    print ("Sorry an error has occurred.")  # Give warning if the csv file doesn't exist

for row in reader:
    if row['Region'] not in regionsname:
        regionsname.append (row['Region'])  # add the region's name if it's not already in the list
# Depending on the name of regions, add up the units sold and Total revenue
    if row['Region'] == "Sub-Saharan Africa":
        TUnitSold1  += int (row['Units Sold'])
        TRevenu1    += float (row['Total Revenue'])
    elif row['Region'] == "Middle East and North Africa":
        TUnitSold2  += int (row['Units Sold'])
        TRevenu2    += float (row['Total Revenue'])
    elif row['Region'] == "Australia and Oceania":
        TUnitSold3  += int (row['Units Sold'])
        TRevenu3    += float (row['Total Revenue'])
    elif row['Region'] == "Europe":
        TUnitSold4  += int (row['Units Sold'])
        TRevenu4    += float (row['Total Revenue'])
    elif row['Region'] == "Asia":
        TUnitSold5  += int (row['Units Sold'])
        TRevenu5    += float (row['Total Revenue'])
    elif row['Region'] == "Central America and the Caribbean":
        TUnitSold6  += int (row['Units Sold'])
        TRevenu6    += float (row['Total Revenue'])
    elif row['Region'] == "North America":
        TUnitSold7  += int (row['Units Sold'])
        TRevenu7    += float (row['Total Revenue'])
    else:   # Ideally it shouldn't happen
        print("There are some regions with invalid name!")

# put all above calculations into the list for printing in the report
TotalUnitSoldList   = [TUnitSold1, TUnitSold2, TUnitSold3, TUnitSold4, TUnitSold5, TUnitSold6, TUnitSold7]
TotalRevenueOfSale  = [TRevenu1, TRevenu2, TRevenu3, TRevenu4, TRevenu5, TRevenu6, TRevenu7]
AvgRevenuPerUnit    = [TRevenu1 / TUnitSold1, TRevenu2 / TUnitSold2, TRevenu3 / TUnitSold3, TRevenu4 / TUnitSold4,
                    TRevenu5 / TUnitSold5, TRevenu6 / TUnitSold6, TRevenu7 / TUnitSold7]

# Generate the report
ReportLine1 = "Sales Report"
ReportLine2 = "------------"
ReportLine3 = "Produced on: " + str (datetime.date.today ())  # Generate the date of report using time library

print (ReportLine1.center (150, ' ') + "\n" + ReportLine2.center (150, ' ') + "\n")
print ((ReportLine3.center (150, ' ')) + "\n")
print ("Regions analysed: ", end='')
print (*regionsname, sep=", ")
print ("\nTotal, %d regions." % len (regionsname) + "\n")

for i in range (len (regionsname)):
    print (regionsname[i] + "\n")
    print ("\tTotal units sold:            %d" % (TotalUnitSoldList[i]))
    print ("\tAverage revenue per unit:    $%.2f" % (AvgRevenuPerUnit[i]))
    print ("\tTotal revenue of sales:      $%.2f" % (TotalRevenueOfSale[i]) + "\n")

print ("Grand Totals\n")
print ("\tTotal units sold:            %d" % (sum (TotalUnitSoldList)))
print ("\tAverage revenue per unit:    $%.2f" % (sum (AvgRevenuPerUnit) / len (AvgRevenuPerUnit)))
print ("\tTotal revenue of sales:      $%.2f" % (sum (TotalRevenueOfSale)))
