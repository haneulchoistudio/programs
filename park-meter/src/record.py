from json import load, dumps

DB_PATH = "cars.json"

def lock_vehicle(cars: dict, car_number: str, time: str):
    if car_number in cars:
        print(f"[X]\tVehicle [{car_number}] is ALREADY in the parking list.")
        return False
    return {
        "plate": car_number,
        "time_in": time,
        "time_out": None
    }
def unlock_vehicle(cars: dict, car_number: str, time: str):
    if car_number not in cars:
        print(f"[X]\tVehicle [{car_number}] is NOT in the parking list.")
        return False
    cars[car_number]['time_out'] = time
    released_vehicle = cars.pop(car_number)
    return released_vehicle
def load_cars() -> dict:
    return load(open(DB_PATH))
def save_cars(cars: dict):
    content = dumps(cars, indent=4)
    with open(DB_PATH, "w") as f:
        f.write(content)
        f.close()
    return True
    