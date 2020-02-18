import os
import csv
file=os.path.join("budget_data.csv")
date=[]
PL=[]
diff=[]
with open(file,newline='')as text:
    budget=csv.reader(text,delimiter=',')
    title=next(budget)
    
    for row in budget:
        date.append(row[0])
        PL.append(int(row[1]))
    for i in range(1,len(PL)):
        diff.append(PL[i]-PL[i-1])
        
    averagechange=round( sum(diff) / (len(PL)-1) ,2)
    a=diff.index(max(diff))
    b=diff.index(min(diff))

print("Financial Analysis")
print("-----------------------------")
print(f'Total Months: {len(date)}')
print(f'Total: ${sum(PL)}')
print(f'Average Change: ${averagechange}')
print(f'Greatest Increase in Profits: {date[a+1]} (${max(diff)})')
print(f'Greatest Increase in Profits: {date[b+1]} (${min(diff)})')

out=os.path.join('PyBank_outputfile')
with open(out,'w',newline='') as outfile:
    outfile.write('Fiancial Analysis\n')
    outfile.write('-----------------------------\n')
    outfile.write(f'Total Months: {len(date)}\n')
    outfile.write(f'Average Change $: {averagechange}\n')
    outfile.write(f'Greatest Increase in Profits: {date[a+1]} (${max(diff)})\n')
    outfile.write(f'Greatest Increase in Profits: {date[b+1]} (${min(diff)})\n')

