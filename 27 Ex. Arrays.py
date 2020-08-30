# Task

# Make an array called houses containing the
# 4 senior boys houses. Perform the following tasks

# 1. Add a fifth house called Williams
# 2. Remove Summerfield
# 3. display every other house















# ------- Solution -------

houses = [ "Sutton","School","Hazelveare","Summerfield"]
houses.append("Williams")
houses.remove("Summerfield")
print(houses)
for x in range(0,len(houses)-1,2):
    print(houses[x])