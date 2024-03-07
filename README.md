# python-challenge

## This is the repo for Module 3 Challenge

The code was done with the material learned during class, reviewing the zoom recordings and also with help of ChatGPT.

For the first activity **"PyBank"**, I mainly used AI to help me understand how to determine the variables of greatest increase and greatest decrease. Finally I also did not know how to export the results to a text file and asked ChatGPT how to do it.

`greatest_increase=["",0]`
`greatest_decrease=["",9999999999]`

`with open(output_file,'w') as txtfile:`
    `txtfile.write('Financial Analysis\n')`
    `txtfile.write('---------------------------------\n')`
    `txtfile.write(f'Total Months: {total_months}\n')`
    `txtfile.write(f'Total: ${net_total}\n')`
    `txtfile.write(f'Average Change: ${average_change:.2f}\n')`
    `txtfile.write(f'Greatest Increase in Profits: {greatest_increase[0]}(${greatest_increase[1]})\n')`
    `txtfile.write(f'Greatest Increase in Profits: {greatest_decrease[0]}(${greatest_decrease[1]})\n')`

`print(f'Results exported to {output_file}')`

For the second activity **"PyPoll"**, I first had a mistake with the candidates variables, and upon asking ChatGPT, I learned I mistakenly used a list instead of a dictionary. Then I also used AI to determine how to format the percentage as a floating point number with decimal places.

`for candidate, votes in candidates.items():`
    `percentage=(votes/total_votes)*100`
   ` print(f'{candidate}: {percentage:.3f}% ({votes})')`
