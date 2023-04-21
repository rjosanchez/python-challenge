# Import modules to read and write csv file
import os
import csv

# Designate the path to collect data from the csv file in the Resources folder
csvpath = os.path.join('Resources', 'budget_data.csv')

#Read the csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # skip the header
    next(csvfile, None)
   
    # Set initial lists
    months = []
    profits = []
    change = []

    # add data to my lists
    for row in csvreader: 
        month = row[0]
        profit = int(row[1])

        months.append(month)
        profits.append(profit)

        # Caluculate the total number of months included in the dataset
        monthscount = len(months)

    # Calculate net total amount of "Profit/Losses" over the entire period
        profittotal = sum(profits)

    # Calculate the changes in Profit/Losses over the entire period
    for x in range(len(profits)-1):
        change.append(profits[x+1]-profits[x])
    
    # Calculate the average P&L Change
    avgchange = sum(change)/len(change)
    avgchange = round(avgchange, 2)

    # Calculate the greatest increase in profits (max value)
    maxchange = max(change)
    
    # Calculate the greaatest decrease in profits (min value)
    minchange = min(change)

    # find date for maxchange and minchange
 
        
    # Print Financial Analysis
    print ("Financial Analysis")
    print ("------------------------------")
    print (f"Total Months: " + str(monthscount))
    print (f"Total: $" + str(profittotal))
    print (f"Average Change: $" + str(avgchange))
    print (f"Greatest Increase in Profits: ($" + str(maxchange) + ")")
    print (f"Greatest Decrease in Profits: ($" + str(minchange) + ")")

# Write analysis to new text file
report = open('financial-analysis.txt', 'w')
report.write ("Financial Analysis" + '\n')
report.write ("------------------------------" + '\n')
report.write (f"Total Months: " + str(monthscount) + '\n')
report.write (f"Total: $" + str(profittotal) + '\n')
report.write (f"Average Change: $" + str(avgchange) + '\n')
report.write (f"Greatest Increase in Profits: ($" + str(maxchange) + ")" + '\n')
report.write (f"Greatest Decrease in Profits: ($" + str(minchange) + ")")
report.close()




           


           
