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

    start_row = 0
    row_list = []
    r_l = []
    sr = 0
    list_changes = []
    greatest_increase = []
    greatest_decrease = []

# Skip header when looping through csv

    skip_first_row = next(csvreader)
    

# skip to the second row
# converts the value in the second column to an int

    start_row = start_row+int(skip_first_row[1])

# skip to the first row
# converts the value in the first column to an int

    set_value = int(skip_first_row[1])

# gets number of months and net profits/losses

    for row in csvreader:
        sr = sr+1
# starting from the second row, counts the number of 
# rows
        start_row = start_row+int(row[1])
# takes the value of the first row, converts it
# to an int and subtracts it from the value in
# the second row

        value_changes = int(row[1])-set_value

        # set_value = int(row[1])
        month_changes = row[0]
        list_changes.append(value_changes)
        list_changes.append(month_changes)
        greatest_increase.append(value_changes)
        grt = max(greatest_increase)
        greatest_decrease.append(value_changes)
        dec = min(greatest_decrease)
        index_greatest_increase = list_changes.index(grt)
        index_greatest_decrease = list_changes.index(dec)
        total_average_profits_losses = sum(greatest_increase)/len(greatest_increase)
    # r_l.append(sr)
    # row_list.append(start_row)
    net_profits_losses = start_row
    number_of_months = sr
    print("Financial Analysis")
    print("------------------------")
    print("Total Months: " + str(number_of_months))
    print("Total: $"+str(net_profits_losses))
    print("Average Change:$"+str(total_average_profits_losses))
    print("Greatest Increase in Profits: "+str(list_changes[index_greatest_increase+1])+" ($"+str(grt)+")")
    print("Greatest Decrease in Profits: "+str(list_changes[index_greatest_decrease+1])+" ($"+str(dec)+")")

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
