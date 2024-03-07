import os
import csv

#path to csv file

csvpath=os.path.join('Resources','budget_data.csv')

#initializing variables

total_months=0
net_total=0
prev_profit_loss=0
total_change=0
greatest_increase=["",0]
greatest_decrease=["",9999999999]

#read csv file

with open(csvpath,newline="") as csvfile:
    csvreader=csv.reader(csvfile)

    #skip header row

    csv_header=next(csvreader)

    #loop through rows in csv file

    for row in csvreader:

        #update total months

        total_months=total_months+1

        #update net total

        net_total=net_total+int(row[1])

        #calculate change in profits and losses

        if total_months>1:
            change=int(row[1])-prev_profit_loss
            total_change=total_change+change

            #check greatest incrase and decrease

            if change>greatest_increase[1]:
                greatest_increase=[row[0],change]

            if change<greatest_decrease[1]:
                greatest_decrease=[row[0],change]

        #update previous profit or loss
        prev_profit_loss=int(row[1])

#calculate average change
        
average_change=total_change/(total_months-1)

#print analysis in terminal and export results to a text file
output_file=os.path.join('Analysis','financial_analysis.txt')

print('Financial Analysis')
print('---------------------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${net_total}')
print(f'Average Change: ${average_change:.2f}')
print(f'Greatest Increase in Profits: {greatest_increase[0]}(${greatest_increase[1]})')
print(f'Greatest Increase in Profits: {greatest_decrease[0]}(${greatest_decrease[1]})')

with open(output_file,'w') as txtfile:
    txtfile.write('Financial Analysis\n')
    txtfile.write('---------------------------------\n')
    txtfile.write(f'Total Months: {total_months}\n')
    txtfile.write(f'Total: ${net_total}\n')
    txtfile.write(f'Average Change: ${average_change:.2f}\n')
    txtfile.write(f'Greatest Increase in Profits: {greatest_increase[0]}(${greatest_increase[1]})\n')
    txtfile.write(f'Greatest Increase in Profits: {greatest_decrease[0]}(${greatest_decrease[1]})\n')

print(f'Results exported to {output_file}')
