import json

f=open('lab2\ex2-text.csv','r')
csvText=f.readlines()
f.close()

csvTextStriped=[]
for row in csvText:
    csvTextStriped.append(row.strip('\n'))

csvTextStripedAndParsed=[]
for row in csvTextStriped:
    csvTextStripedAndParsed.append(row.split(','))

employees=[]
for i in range(1,len(csvTextStripedAndParsed)):
    employee={}
    employee['employee']=csvTextStripedAndParsed[i][0]
    employee['title']=csvTextStripedAndParsed[i][1]
    employee['age']=int(csvTextStripedAndParsed[i][2])
    employee['office']=csvTextStripedAndParsed[i][3]
    employees.append(employee)

print(employees)

with open('lab2\ex4-employees.json', 'w', encoding='utf-8') as f:
    json.dump(employees, f)
    