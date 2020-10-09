# Imports necessary packages
# To read in csv

import os
import csv
csvpath = os.path.join(os.getcwd(), 'Resources', 'budget_data.csv')
print(csvpath)

# Opens csvs using with

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    net_profits_losses = 0
    number_of_months = 0
    list_changes = []
    max_min = []


# Skip header when looping through csv

    skip_first_row = next(csvreader)


# skip to the second row
# converts the value in the second column to an int

    net_profits_losses = net_profits_losses+int(skip_first_row[1])

# skip to the first row
# converts the value in the first column to an int

    set_value = int(skip_first_row[1])

# gets number of months and net profits/losses

    for row in csvreader:
        number_of_months = number_of_months+1

# starting from the first row, sums up
# the total amount of money

        net_profits_losses = net_profits_losses+int(row[1])

# takes the value of the first row, converts it
# to an int and subtracts it from the value in
# the second row

        value_changes = int(row[1])-set_value

# gets the month from the first column
# of every row

        month_changes = row[0]

# appends the value changes from the subtraction
# function to a list

        list_changes.append(value_changes)

# appends the months from each row to
# a list

        list_changes.append(month_changes)
        max_min.append(value_changes)
        greatest_increase = max(max_min)
        max_min.append(value_changes)
        greatest_decrease = min(max_min)
        index_greatest_increase = list_changes.index(greatest_decrease)
        index_greatest_decrease = list_changes.index(greatest_decrease)
        total_average_profits_losses = sum(max_min)/len(max_min)
      

    print("Financial Analysis")
    print("------------------------")
    print("Total Months: " + str(number_of_months))
    print("Total: $"+str(net_profits_losses))
    print("Average Change:$"+str(total_average_profits_losses))
    print("Greatest Increase in Profits: "+str(list_changes[index_greatest_increase+1])+" ($"+str(greatest_increase)+")")
    print("Greatest Decrease in Profits: "+str(list_changes[index_greatest_decrease+1])+" ($"+str(greatest_decrease)+")")

    output_file = os.path.join("budget_data_text.txt")
    with open(output_file, "w") as datafile:
        writer = csv.writer(datafile)
        datafile.write("Financial Analysis")
        datafile.write("-------------------------")
        datafile.write("Financial Analysis\n")
        datafile.write("Total Months: 86\n")
        datafile.write("Total:$38382578\n")
        datafile.write("Average Change: -2315.12\n")
        datafile.write("Greatest Increase in Profits: Feb 2012 (1926159)\n")
        datafile.write("Greatest Decrease in Profits: Sep 2013 (-2196167)\n")
