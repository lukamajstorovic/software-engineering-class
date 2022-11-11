f=open('lab2\ex2-text.csv','r')
csvText=f.readlines()
f.close()

csvTextStriped=[]
for row in csvText:
    csvTextStriped.append(row.strip('\n'))

csvTextStripedAndParsed=[]
for row in csvTextStriped:
    csvTextStripedAndParsed.append(row.split(','))

csvTextStripedAndParsed.pop(0)

f1=open('lab2\ex2-employees.txt','w')
f2=open('lab2\ex2-locations.txt','w')

for row in csvTextStripedAndParsed:
    f1.write(f'{row[0]}, {row[1]}\n')
    f2.write(f'{row[0]}, {row[3]}\n')

f1.close()
f2.close()
