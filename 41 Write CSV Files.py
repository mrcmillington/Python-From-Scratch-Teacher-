# Demo ( Copy the code below )
import csv

file=open("44 singers.txt","w")
writer = csv.writer(file,lineterminator = '\n')
writer.writerow(["Anastacia",26])
writer.writerow(["Ariana Grande",23])
file.close()


# Task

# Write a program to store users names
# and  e-mail addresses

















print(" ------- Task -------")
x=0
while x<4:
    name = input("What is your name")
    eMail = input("What is your e-mail")
    fl = open("41-eMails.txt", "a")
    writer = csv.writer(fl, lineterminator='\n')
    j = [name, eMail]
    print(j)
    writer.writerow(j)
    fl.close()
    x+=1




