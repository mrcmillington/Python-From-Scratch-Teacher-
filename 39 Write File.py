# Demo ( Copy the code below )
f = open("42 file.txt", "w")
f.write("Oops I did it again")
f.close()


# Task
# Can you modify this program so it adds
# the next line of the song, and then
# reads out the conents of the file to
# the terminal
















print("------- Task -------")

f = open("42 file.txt", "w")
f.write("Oops I did it again, ")
f.write("I played with your heart, got lost in the game")
f.close()

f = open("42 file.txt", "r")
print(f.read())



