# Task

# Write a program for a till.
# - You should write 1 function to multiply the
#   quantity and the price
# - Write a second function to add 17.5% sales tax
# - Display the output
















print(" ------- Task -------")

def total(prc,quan):
    return prc*quan
def tax(prc):
    return prc*1.175
price = int(input("How much are they ?"))
quantity = int(input("How many do you want ?"))
print(tax(total(price,quantity)))



