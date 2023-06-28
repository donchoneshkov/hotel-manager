

def populate_level(level):


    # =========================== apply map to level
    mapping = {
                0: {'category' : 'ground_tiles' , 'type': 'grass'}, 
                1: {'category' : 'ground_tiles' , 'type': 'brick'},
                2: {'category' : 'ground_tiles' , 'type': 'concrete'},
                3: {'category' : 'ground_tiles' , 'type': 'wood'},
                4: {'category' : 'ground_tiles' , 'type': 'marble'},
                100: {'category' : 'furniture_tiles', 'type': 'sofa'},
                200: {'category' : 'appliance_tiles', 'type': 'tv'},
                900: {'category' : 'entry_tiles', 'type' : 'entry'}
            }

    for i in range(len(level)):
        for j in range(len(level[i])):
            value = level[i][j]
            if value in mapping:
                level[i][j] = mapping[value]

    # =========================== populate level map with coords and values
    level_map = []
    for row in range(len(level)):
        for col in range(len(level[row])):
            level_map.append([[row, col], level[col][row]]) 
    # print(level_map)
    return level_map