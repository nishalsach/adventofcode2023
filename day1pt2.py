import re

f = open("input/day1.txt", "r")
total = 0

# Init the matching from spelling to nums
spelling_values = {
    'zero': 0, 
    'one': 1, 
    'two': 2, 
    'three': 3, 
    'four': 4, 
    'five': 5, 
    'six': 6, 
    'seven': 7, 
    'eight': 8, 
    'nine': 9
}

# Keys and regex
# keys_piped = '|'.join(spelling_values)
regex = re.compile("(?=(" + "|".join(map(re.escape, spelling_values)) + "|\d"+"))")

# Iterate
for calval in f.readlines():

    # Use regex to find digits -- this will use a lookahead, compile the text AND the numeric digits into an OR condition
    digits_list = re.findall(regex, calval.strip())
    digits_list = [digits_list[0]] + [digits_list[-1]] # Update to just keep important ones
    digits_list = [spelling_values[i] if len(i)>1 else int(i) for i in digits_list]
    
    #print(digits_list)
    
    # With the flattened list, do the math
    actual_value = digits_list[0]*10 + digits_list[-1]
    total+=actual_value
    
print(total)
