import re

# Read in
f = open("input/day2.txt", "r")
# Init a value
total = 0
game_num = 0

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

    
# Iterate over readlines
for game in f.readlines():
    
    game_num+=1
    should_game_count = True # -- start from a position where the game definitely counts
    
    # Extract list of rounds
    round_list = game.split(':')[1].split(';')
    
    # Iterate over rounds
    for game_round in round_list:
        
        # Get the numbers
        num_red = find_color_count(game_round, 'r')
        num_blu = find_color_count(game_round, 'b')
        num_gre = find_color_count(game_round, 'g')
        
        # check breaking conditions -- 
        if (num_red <= 12) & (num_blu <= 14) & (num_gre <= 13):
            continue
        else: 
            should_game_count = False
            break
            
    if should_game_count:
        total+=game_num
            
print(total)