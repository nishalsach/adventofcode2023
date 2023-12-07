import re

def find_color_count(game_round, color):
    
    # f-string with regex to find color
    pattern = rf'\d+\s[{color}]'
    
    # Match the template for this color
    color_matches = re.findall(pattern, game_round)
    
    # if list exists i.e. is non-empty
    if color_matches:
        return int(color_matches[0].split(' ')[0])
    else:
        return 0
    
# Read in
f = open("input/day2.txt", "r")

# Init a value
powers_sum = 0

# Iterate over readlines
for game in f.readlines():
    
    # Init the max needed for each colour
    max_red = 0
    max_blu = 0
    max_gre = 0

    # Extract list of rounds
    round_list = game.split(':')[1].split(';')
    
    # Iterate over rounds
    for game_round in round_list:
        
        # Get the numbers
        num_red = find_color_count(game_round, 'r')
        num_blu = find_color_count(game_round, 'b')
        num_gre = find_color_count(game_round, 'g')
        
        # Now just set the max variables to being max of what has been done and what was captured
        max_red = max(max_red, num_red)
        max_blu = max(max_blu, num_blu)
        max_gre = max(max_gre, num_gre)
        
    # The power of this game
    game_power = max_red*max_blu*max_gre

    # Add
    powers_sum+=game_power
            
print(powers_sum)