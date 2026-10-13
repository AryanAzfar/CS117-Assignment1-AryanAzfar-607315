# Finding the total resistances

count = int(input("How many resistors? "))                    #using "int" becuse we want integer as input from user

total_resistance = 0                                          #initial resistance before loop runs

#we are using (for loop) here
for i in range(1, count + 1):                               #specifying the range for loop to run
    resistance = float(input("Enter R" + str(i) + ": "))       #str(i): Converts the number i into text so it can be glued together with other text
    total_resistance = total_resistance + resistance
#for displying outputs
print("Total resistance =", total_resistance, "ohm")
