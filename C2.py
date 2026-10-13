# C2. Parallel Resistance 

# Formula: 1 / Req = 1/R1 + 1/R2 + ..........



def parallel_resistance(resistors):   #Defining a function to calculate the total equivalent resistance for resistors connected in parallel
    reciprocal_sums = 0                # Initialization for the sum of reciprocals (1/R)
    #using for loop inside the funnction
    for r in resistors:
        reciprocal_sums = reciprocal_sums + 1 / r          # Add the reciprocal of the current resistor
    return round(1 / reciprocal_sums, 2)

# checking the function with a pair of 10-ohm resistors
print("parallel_resistance([10, 10]) ->", parallel_resistance([10, 10]))    
# checking the function with three different resistors
print("parallel_resistance([100, 200, 300]) ->", parallel_resistance([100, 200, 300]))      
