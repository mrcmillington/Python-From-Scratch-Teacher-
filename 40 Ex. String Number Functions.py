# Task

# You have been asked to decrypt a secret message.
# You need to display every other letter in order
# to read it . Write a program to do this


# cgojmfpauftgijnkgrrkolclkss














print(" ------- Task -------")

encrypt = "cgojmfpauftgijnkgrrkolclkss"
decrypt = ""
for x in range(0,len(encrypt),2):
    decrypt += encrypt[x]
print(decrypt)



