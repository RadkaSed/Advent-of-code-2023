games = {}

with open('input_2.txt', mode='r', encoding='utf-8') as input_file:
    content = (line.strip() for line in input_file if line.strip())


    for line in content:
        game_num, game_content = line.split(':')
        game_number = int(game_num.split()[1])
        game_part = game_content.split(';')
        game_dict = []
        for part in game_part:
            part_dict = {}
            items = part.split(',')
            for item in items:
                value, colour = item.split()
                part_dict[colour] = int(value)
            game_dict.append(part_dict)
        
        games[game_number] = game_dict
        

real_cubes = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def is_valid_game(game_cubes, real_cubes):
    for part_dict in game_cubes:
        for colour, value in part_dict.items():
            if colour in real_cubes and value > real_cubes[colour]:
                return False
    return True


real_games = [game_num for game_num, game_cubes in games.items() if is_valid_game(game_cubes, real_cubes)]

games_cubes_multiplies = []

min_cubes_for_game = []  

for game_num, game_content in games.items():
    game_min_cubes = {}
    min_cubes = {'blue': 0, 'red': 0, 'green': 0}
    for part_dict in game_content:
        for colour, value in part_dict.items():
            if colour in min_cubes and part_dict[colour] > min_cubes[colour]:
                min_cubes[colour] = value
    game_min_cubes[game_num] = min_cubes     
    min_cubes_for_game.append(game_min_cubes)
    
for game in min_cubes_for_game:
    for game_num, game_content in game.items():
        multiply_result = 1
        for colour, value in game_content.items():
            multiply_result *= value
        games_cubes_multiplies.append(multiply_result)
        
print(sum(games_cubes_multiplies))