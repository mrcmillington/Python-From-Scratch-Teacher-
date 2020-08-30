# Demo ( Copy the code below )
import random
print(random.randrange(1,10))


# Task
# Write a program to ask for a random letter
# from a preset keyword. The keyword is computing
















print(" ------- Task -------")

key = "computing"
number = random.randrange(0,len(key))
letter = key[number]
print(letter)
print("Please enter letter number ",number+1 ,"  from the key")
answer = input()
if answer==letter:
    print("Welcome friend")
else:
    print("Begone foul beast")


