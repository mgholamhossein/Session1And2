import pandas
import os
import datetime

if os.path.exists ('500000 Sales Records.csv'):             # check the existence of the csv file using os library
    df = pandas.read_csv ('500000 Sales Records.csv')       # create the data frame from csv file using pandas library
else:
    print ("Sorry an error has occurred.")

# a- The number of total units sold for the region
x = df.groupby (df.Region)['Units Sold'].sum ()             # Filter data based on Region and calculate the summation of units sold for each group

# c- The total revenue for the region
y = df.groupby (df.Region)['Total Revenue'].sum ()          # Filter data based on Region and calculate the summation of Total Revenue for each group

# b- The average revenue of all the units sold for the region
z = y / x


ReportLine1 = "Sales Report"
ReportLine2 = "------------"
ReportLine3 = "Produced on: " + str(datetime.date.today())  # Generate the date of report using time library
uniqueValues = df['Region'].unique()                        # extract Regions from data frame

print (ReportLine1.center(150,' ') + "\n" + ReportLine2.center(150,' ') + "\n" )
print ((ReportLine3.center(150,' '))+"\n")
print("Regions analysed: ", end='')
print(*uniqueValues, sep = ", ")
print("\nTotal, %d regions."%len(uniqueValues) + "\n")

for i in uniqueValues:
    print (i+"\n")
    print("\tTotal units sold:            %d" %(x[i]))
    print ("\tAverage revenue per unit:    $%.2f" %(z[i]))
    print ("\tTotal revenue of sales:      $%.2f" %(y[i]) + "\n")

print("Grand Totals\n")
print("\tTotal units sold:            %d" %(x.sum()))
print ("\tAverage revenue per unit:    $%.2f" %(z.sum()/len(z)))
print ("\tTotal revenue of sales:      $%.2f" %(y.sum()))










