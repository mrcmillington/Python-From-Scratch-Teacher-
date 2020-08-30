import csv
file=open("44 singers.txt","r")
reader = csv.reader(file)
for row in reader:
    if int(row[1])>25:
        print(row)
file.close()