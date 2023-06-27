

def populate_level(level):


    # =========================== apply map to level
    mapping = {
                0: {'category' : 'ground_tiles' , 'type': 'grass'}, 
                1: {'category' : 'ground_tiles' , 'type': 'brick'},
                2: {'category' : 'ground_tiles' , 'type': 'concrete'},
                3: {'category' : 'ground_tiles' , 'type': 'wood'},
                4: {'category' : 'ground_tiles' , 'type': 'marble'},
            }

    for i in range(len(level)):
        for j in range(len(level[i])):
            value = level[i][j]
            if value in mapping:
                level[i][j] = mapping[value]
                print(mapping[value])

    # =========================== populate level map with coords and values
    level_map = []
    for row in range(len(level)):
        for col in range(len(level[row])):
            level_map.append([[row, col], level[col][row]]) 
    # print(level_map)
    return level_map