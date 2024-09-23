from generateCorporations import generate_corporations
from generateMap import generate_map
from generateScenario import generate_scenario

# ========== GENERATE THE MAP ==========

# Define tile categories for the map:
# Shore tiles, shallow ocean tiles, deep ocean tiles, and "no_tile" (areas with no tiles)
shore_tiles = [20, 21]
shallow_ocean_tiles = [17, 18]
deep_ocean_tiles = [1, 2]
no_tile = [41, 43, 44, 48]

# NOTE: All the tiles not specified in the above categories will be the land tiles

categories = [shore_tiles, shallow_ocean_tiles, deep_ocean_tiles, no_tile]

# Define harbor locations
harbors = [20]  # List of tile IDs that have harbors

# Define ocean currents. Format: {tile_id: [velocity, acceleration, direction]}
currents = {
    2: [300, 10, 5]  # Tile 2 has a current with 300 velocity, 10 acceleration, and 5 direction
}

# Map size
rows = 8        # Number of rows in the map
columns = 6     # Number of columns in the map

# Define the name of the map file to save the JSON output
name_of_map_file = 'map'

# Call the generate_map function
generate_map(rows, columns, categories, harbors, currents, name_of_map_file)



# ========== GENERATE THE CORPORATIONS ==========

# Define types of garbage
plastic = "PLASTIC"
oil = "OIL"
chemicals = "CHEMICALS"

# Define types of ships
scouting = "SCOUTING"
collecting = "COLLECTING"
coordinating = "COORDINATING"

# Define the name of the corporation file to save the JSON output
name_of_corp_file = "corp"

# Number of corporations to generate
num_of_corps = 2

# Define ship details for each corporation.
# Format: (ship_type, corporation_id, location, max_velocity, acceleration, fuel_capacity, fuel_consumption, visibility_range)
ship_details = [
    (scouting, 1, 3, 200, 25, 3000, 10, 5),
    (collecting, 2, 3, 200, 25, 3000, 10, 5),
    (coordinating, 1, 122, 33, 12, 12, 12, 1)
]

# Define home harbor locations for each corporation.
# Key: corporation ID, Value: list of harbor tile IDs
corp_home_harbors = {
    1: [1, 9, 10],   # Corporation 1 has harbors at tiles 1, 9, and 10
    2: [3, 5]        # Corporation 2 has harbors at tiles 3 and 5
}

# Define the type of garbage each corporation focuses on.
# Key: corporation ID, Value: list of garbage types (can focus on multiple types)
corp_garbage_type = {
    1: [plastic, chemicals],  # Corporation 1 collects plastic and chemicals
    2: [chemicals]            # Corporation 2 collects only chemicals
}

# Call the generate_corporations function
generate_corporations(num_of_corps, ship_details, corp_home_harbors, corp_garbage_type, name_of_corp_file)



# ========== GENERATE THE SCENARIO ==========

# Garbage types
plastic = "PLASTIC"
oil = "OIL"
chemicals = "CHEMICALS"

# Event types
storm = "STORM"
restriction = "RESTRICTION"
oil_spill = "OIL_SPILL"
pirate_attack = "PIRATE_ATTACK"

# Task types
collect = "COLLECT"
explore = "EXPLORE"
find = "FIND"
cooperate = "COOPERATE"

# Reward types
telescope = "TELESCOPE"
radio = "RADIO"
container = "CONTAINER"
tracker = "TRACKER"

# Define the name of the scenario file to save the JSON output
name_of_scenario_file = "scenario"

# Define garbage on the map.
# Format: (garbage_type, location, amount)
garbage = [
    (plastic, 28, 50),
    (oil, 28, 1000),
    (plastic, 3, 100)
]

# Define events on the map.
# Different events have different formats:
# Storm: (event_type, tick, location, radius, speed, direction)
# Restriction: (event_type, tick, duration, location, radius)
# OilSpill: (event_type, tick, location, radius, amount)
# PirateAttack: (event_type, tick, ship_id)
events = [
    (storm, 1, 2, 3, 22, 60),
    (restriction, 1, 2, 12, 2),
    (oil_spill, 1, 2, 3, 1000),
    (pirate_attack, 1, 2)
]

# Define tasks for the ships.
# Format: (task_type, tick, assigned_ship_id, target_tile, reward_id, reward_ship_id)
tasks = [
    (collect, 3, 4, 7, 3, 1),
    (explore, 6, 1, 10, 3, 2),
    (cooperate, 2, 2, 9, 3, 3)
]

# Define rewards for completing tasks.
# Telescope: (reward_type, visibility_range)
# Container: (reward_type, capacity, garbage_type)
# Radio and Tracker: (reward_type)
rewards = [
    (telescope, 3),
    (container, 20, oil),
    tracker,
    radio
]

# Call the generate_scenario function
generate_scenario(garbage, events, tasks, rewards, name_of_scenario_file)
