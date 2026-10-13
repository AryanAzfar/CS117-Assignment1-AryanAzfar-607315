#checking wealther the fuse will blow or not
 

voltage = float(input("Enter voltage (V): "))     #using float because volage and current can be in decimals
resistance = float(input("Enter resistance (ohm): "))

if resistance <= 0:                             # its a condition if resistance is equal or less then zero then
    print("Invalid resistance")
else:
    
    current = voltage / resistance          #applied the I=V/R formula
    print("Current =", current, "A")
    if current > 2:                     #applaying condition
        print("Fuse will blow")
    else:
        print("Circuit is safe")
