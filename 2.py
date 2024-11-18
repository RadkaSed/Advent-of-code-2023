games = {}

with open('input_2.txt', mode='r', encoding='utf-8') as input_file:
    content = input_file.readlines()
    for line in content:
        line = line.strip()
        if line:
            game_num, game_content = line.split(':')
            game_number = int(game_num.split()[1])
            game_part = game_content.split(';')
            game_dict = []
            for part in game_part:
                part_dict = {}
                items = part.split(',')
                for item in items:
                    colour_value = item.split()
                    if len(colour_value) == 2:
                        value = int(colour_value[0])
                        colour = colour_value[1]
                        part_dict[colour] = value
                game_dict.append(part_dict)
            games[game_number] = game_dict
            
real_cubes = {
    'red': 12,
    'green': 13,
    'blue': 14
}
        
real_games = []

for game_num, game_cubes in games.items():
    valid = True 
    for part_dict in game_cubes:
        for colour, value in part_dict.items():
            if colour in real_cubes and value > real_cubes[colour]:
                valid = False 
                break
        if not valid:
            break
    if valid:
        real_games.append(game_num)
            
print(real_games)
            
            
            
sum_of_real_ID = sum(real_games)
print(sum_of_real_ID)