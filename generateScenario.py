import json

def generate_scenario(garbage, events, tasks, rewards, name_of_scenario_file):
    scenario = {
        "garbage": generate_garbage(garbage),
        "events": generate_events(events),
        "tasks": generate_tasks(tasks),
        "rewards": generate_rewards(rewards)
    }

    generate_json(name_of_scenario_file, scenario)


def generate_garbage(garbage_details):
    garbage_list = []
    garbage_id = 1

    for garbage in garbage_details:
        garbage_entry = {
            "id": garbage_id,
            "type": garbage[0],
            "location": garbage[1],
            "amount": garbage[2]
        }
        garbage_list.append(garbage_entry)
        garbage_id += 1

    return garbage_list


def generate_events(event_details):
    events_list = []
    event_id = 1

    for event in event_details:
        event_type = event[0]
        if event_type == "STORM":
            # Storm: type, tick, location, radius, speed, direction
            event_entry = {
                "id": event_id,
                "type": event_type,
                "tick": event[1],
                "location": event[2],
                "radius": event[3],
                "speed": event[4],
                "direction": event[5]
            }
        elif event_type == "RESTRICTION":
            # Restriction: type, tick, duration, location, radius
            event_entry = {
                "id": event_id,
                "type": event_type,
                "tick": event[1],
                "duration": event[2],
                "location": event[3],
                "radius": event[4]
            }
        elif event_type == "OIL_SPILL":
            # Oil Spill: type, tick, location, radius, amount
            event_entry = {
                "id": event_id,
                "type": event_type,
                "tick": event[1],
                "location": event[2],
                "radius": event[3],
                "amount": event[4]
            }
        elif event_type == "PIRATE_ATTACK":
            # Pirate Attack: type, tick, shipID
            event_entry = {
                "id": event_id,
                "type": event_type,
                "tick": event[1],
                "shipID": event[2]
            }

        events_list.append(event_entry)
        event_id += 1

    return events_list


def generate_tasks(task_details):
    tasks_list = []
    task_id = 1

    for task in task_details:
        task_entry = {
            "id": task_id,
            "type": task[0],
            "tick": task[1],
            "assigned_ship_id": task[2],
            "target_tile": task[3],
            "reward_id": task[4],
            "reward_ship_id": task[5]
        }
        tasks_list.append(task_entry)
        task_id += 1

    return tasks_list


def generate_rewards(reward_details):
    rewards_list = []
    reward_id = 1

    for reward in reward_details:
        reward_type = reward[0]
        if reward_type == "TELESCOPE":
            # Telescope: type, visibilityRange
            reward_entry = {
                "id": reward_id,
                "type": reward_type,
                "visibilityRange": reward[1]
            }
        elif reward_type == "CONTAINER":
            # Container: type, capacity, garbageType
            reward_entry = {
                "id": reward_id,
                "type": reward_type,
                "capacity": reward[1],
                "garbageType": reward[2]
            }
        elif reward_type == "TRACKER":
            # Tracker: type
            reward_entry = {
                "id": reward_id,
                "type": reward_type
            }
        elif reward_type == "RADIO":
            # Radio: type
            reward_entry = {
                "id": reward_id,
                "type": reward_type
            }

        rewards_list.append(reward_entry)
        reward_id += 1

    return rewards_list

def generate_json(name, scenario_data):
    with open(f"{name}.json", 'w') as json_file:
        json.dump(scenario_data, json_file, indent=2)