
# all tiles apart from sell and none are here, sell is practically grass
tile_types = {
                'ground_tiles' :
                {
                    'grass' : {
                        'tile_type' : 'ground_tiles', 
                        'tile' : 'grass',
                        'path' : 'img/tiles/grass_tile.png', 
                        'cost' : 0, 
                        'sellable' : True,
                        'passable' : False,
                        'tile_satisfaction' : 0,
                        'use_cost' : 0,
                        'map_value': 0,
                        },
                    'brick' : {
                        'tile_type' : 'ground_tiles', 
                        'tile' : 'brick', 
                        'path' : 'img/tiles/brick_tile.png', 
                        'cost' : 20, 
                        'sellable' : True, 
                        'passable' : False,
                        'tile_satisfaction' : 0,
                        'use_cost' : 0,
                        'map_value': 1,

                        },
                    'concrete' : {
                        'tile_type' : 'ground_tiles', 
                        'tile' : 'concrete', 
                        'path' : 'img/tiles/concrete_tile.png', 
                        'cost' : 15, 
                        'sellable' : True, 
                        'passable' : True,
                        'tile_satisfaction' : -1,
                        'use_cost' : 0,
                        'map_value': 2,

                        },
                    'wood' : {
                        'tile_type' : 'ground_tiles', 
                        'tile' : 'concrete', 
                        'path' : 'img/tiles/wood_tile.png', 
                        'cost' : 10, 
                        'sellable' : True, 
                        'passable' : True,
                        'tile_satisfaction' : 0,
                        'use_cost' : 0,
                        'map_value': 3,

                        },
                    'marble' : {
                        'tile_type' : 'ground_tiles', 
                        'tile' : 'marble', 
                        'path' : 'img/tiles/marble_tile.png', 
                        'cost' : 30, 
                        'sellable' : True, 
                        'passable' : True,
                        'tile_satisfaction' : 1,
                        'use_cost' : 0,
                        'map_value': 4,
                        },
                },
                'furniture_tiles' :
                {
                    'sofa' : {
                        'tile_type' : 'furniture_tiles', 
                        'tile' : 'sofa', 
                        'path' : 'img/furniture/sofa.png', 
                        'cost' : 100, 
                        'sellable' : True, 
                        'passable' : True,
                        'tile_satisfaction' : 5,
                        'use_cost' : 5,
                        'map_value': 100
                        },
                },
                'appliance_tiles' :
                {
                    'tv' : {
                        'tile_type' : 'appliance_tiles', 
                        'tile' : 'tv', 
                        'path' : 'img/appliances/tv.png', 
                        'cost' : 250, 
                        'sellable' : True, 
                        'passable' : True,
                        'tile_satisfaction' : 10,
                        'use_cost' : 15,
                        'map_value': 200
                        },
                    'atm' : {
                        'tile_type' : 'appliance_tiles', 
                        'tile' : 'atm', 
                        'path' : 'img/appliances/atm.png', 
                        'cost' : 500, 
                        'sellable' : True, 
                        'passable' : True,
                        'tile_satisfaction' : 10,
                        'use_cost' : -50,
                        'map_value': 201
                        },
                },
                'entry_tiles' :
                {
                    'entry' : {
                        'tile_type' : 'entry_tiles', 
                        'tile' : 'entry', 
                        'path' : 'img/other/entry.png', 
                        'cost' : 0, 
                        'sellable' : False, 
                        'passable' : True,
                        'tile_satisfaction' : 0,
                        'use_cost' : 0,
                        'map_value': 900
                    }
                }
              }
