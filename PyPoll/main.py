import os
import csv
file=os.path.join('election_data.csv')
Voter=[]
Candidate=[]
num_Khan=0
num_Correy=0
num_Li=0
num_Tooley=0

with open(file,newline='')as text:
    election=csv.reader(text,delimiter=',')
    header=next(election)
    for row in election:
        Voter.append(row[0])
        Candidate.append(row[2])
    for i in Candidate:
        if i=='Khan':
            num_Khan+=1
        elif i=='Li':
            num_Li+=1
        elif i=='Correy':
            num_Correy+=1
        else:
            num_Tooley+=1
               
    total=len(Voter)
    per_Khan= format(num_Khan / total,".3%")
    per_Li= format(num_Li / total,".3%")
    per_Correy= format(num_Correy / total,".3%")
    per_Tooley= format(num_Tooley / total,".3%")
    dic={'Khan':per_Khan,'Correy':per_Correy,'Li':per_Li,'OTooley':per_Tooley}
    max_key=max(dic,key=dic.get)
    
    print("Election Results")
    print("------------------------")
    print(f'Total Votes: {total}')
    print("------------------------")
    print(f'Khan: {per_Khan} ({num_Khan})')
    print(f'Correy: {per_Correy} ({num_Correy})')
    print(f'Li: {per_Li} ({num_Li})')
    print("O'Tooley: "+ str(per_Tooley) +" " +"(" +str(num_Tooley)+")")
    print("------------------------")
    print(f'Winner is: {max_key}')
    print("------------------------")
    
outfile=os.path.join('PyPoll_outputfile')
with open(outfile,'w',newline='')as text:
    text.write("Election Results\n")
    text.write("------------------------\n")
    text.write(f'Total Votes: {total}\n')
    text.write("------------------------\n")
    text.write(f'Khan: {per_Khan} ({num_Khan})\n')
    text.write(f'Correy: {per_Correy} ({num_Correy})\n')
    text.write(f'Li: {per_Li} ({num_Li})\n')
    text.write("O'Tooley: "+ str(per_Tooley) +" " +"(" +str(num_Tooley)+")\n")
    text.write("------------------------\n")
    text.write(f'Winner: {max_key}\n')
    text.write("------------------------\n")

