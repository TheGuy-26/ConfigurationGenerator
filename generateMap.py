import json

def generate_map(rows, columns, categories, harbors, currents, name_of_map):
    tile_grid = generate_tiles(rows, columns, categories, harbors, currents)
    generate_json(name_of_map, tile_grid)

def generate_tiles(rows, columns, categories, harbors, currents):
    shore_tiles, shallow_ocean_tiles, deep_ocean_tiles, no_tile = categories
    tiles = []
    tile_id = 1

    for y in range(rows):
        for x in range(columns):
            if tile_id in shore_tiles:
                if tile_id in harbors:
                    tile = {
                        "id": tile_id,
                        "coordinates": {
                            "x": x,
                            "y": y,
                        },
                        "category": category,
                        "harbors": True
                    }

                else:
                    tile = {
                        "id": tile_id,
                        "coordinates": {
                            "x": x,
                            "y": y,
                        },
                        "category": category,
                        "harbors": False
                    }

                tiles.append(tile)
                tile_id += 1
                continue

            elif tile_id in shallow_ocean_tiles:
                category = "SHALLOW_OCEAN"

            elif tile_id in deep_ocean_tiles:
                if tile_id in currents:
                    current_data = currents[tile_id]
                    tile = {
                        "id": tile_id,
                        "coordinates": {
                            "x": x,
                            "y": y,
                        },
                        "category": "DEEP_OCEAN",
                        "current": True,
                        "direction": current_data[0],
                        "speed": current_data[1],
                        "intensity": current_data[2]
                    }

                else:
                    tile = {
                        "id": tile_id,
                        "coordinates": {
                            "x": x,
                            "y": y,
                        },
                        "category": "DEEP_OCEAN",
                        "current": False
                    }

                tiles.append(tile)
                tile_id += 1
                continue

            elif tile_id in no_tile:
                tile_id += 1
                continue
            else:
                category = "LAND"

            tile = {
                "id": tile_id,
                "coordinates": {
                    "x": x,
                    "y": y,
                },
                "category": category
            }
            tiles.append(tile)
            tile_id += 1

    return {"tiles": tiles}


def generate_json(name, tiles):
    with open(f"{name}.json", 'w') as json_file:
        json.dump(tiles, json_file, indent=2)