import re

# Read in
f = open("input/day1.txt", "r")
# Init a value
total = 0

# Iterate over readlines
for calval in f.readlines():
    
    # Use regex to find digits
    digits_list = re.findall(r'\d', calval)
    
    # With the flattened list, do the math
    actual_value = int(digits_list[0])*10 + int(digits_list[-1])
    total+=actual_value
        
print(total)