import json



def generate_corporations(num_of_crops, ships, corp_home_harbors, corp_garbage_type, name_of_corporation_file):
    corp_and_ships = generate_corporations_and_ships(num_of_crops, ships, corp_home_harbors, corp_garbage_type)
    generate_json(name_of_corporation_file, corp_and_ships)


def generate_corporations_and_ships(num_of_corps, ship_details, corp_home_harbors, corp_garbage_type):
    corporations = []
    ships = []
    corp_to_ships = [[] for _ in range(num_of_corps)]  # Create a list for each corporation

    ship_id = 1
    scouting_id = 1
    collecting_id = 1
    coordinating_id = 1

    for ship in ship_details:
        if ship[0] == "SCOUTING":
            name = "scouting" + str(scouting_id)
            scouting_id += 1
            ship_type = "SCOUTING"
        elif ship[0] == "COLLECTING":
            name = "collecting" + str(collecting_id)
            collecting_id += 1
            ship_type = "COLLECTING"
        elif ship[0] == "COORDINATING":
            name = "coordinating" + str(coordinating_id)
            coordinating_id += 1
            ship_type = "COORDINATING"

        # Adjust the index by subtracting 1 from the corporation ID (1-based to 0-based)
        corp_to_ships[ship[1] - 1].append(ship_id)

        one_ship = {
            "id": ship_id,
            "name": name,
            "type": ship_type,
            "corporation": ship[1],
            "Location": ship[2],
            "maxVelocity": ship[3],
            "acceleration": ship[4],
            "fuelCapacity": ship[5],
            "fuelConsumption": ship[6],
            "visibilityRange": ship[7]
        }

        ships.append(one_ship)
        ship_id += 1

    for corp_id in range(num_of_corps):
        # Get homeHarbor directly from the dictionary using the corporation ID (corp_id + 1)
        homeHarbor = corp_home_harbors.get(corp_id + 1, [])
        garbageType = corp_garbage_type.get(corp_id + 1, [])

        corporation = {
            "id": corp_id,
            "name": "Corporation" + str(corp_id),
            "ships": corp_to_ships[corp_id],
            "homeHarbors": homeHarbor,
            "garbageType": garbageType
        }

        corporations.append(corporation)

    return {
        "corporations": corporations,
        "ships": ships,
    }



def generate_json(name, corp_and_ships):
    with open(f"{name}.json", 'w') as json_file:
        json.dump(corp_and_ships, json_file, indent=2)
