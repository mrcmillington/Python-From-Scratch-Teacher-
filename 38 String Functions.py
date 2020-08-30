# Demo ( Copy the code below )
word = "     AFC Kimbledon"
word = word.strip()
print(word[2])
word = word.replace("K","W")
word = word.lower()
print(word)
print(len(word))

# Task

# Using the Functions above, write a
# program to see if the password a user
# enters is correct. The program should
# ignore capital letters and spaces at
# the start and end

# the password is ploughlane
















print(" ------- Task -------")

password = "ploughlane"
userPW = input("Say the magic word ->")
userPW = userPW.strip()
userPW = userPW.lower()
if password==userPW:
    print("Welcome friend")
else:
    print("begone")


