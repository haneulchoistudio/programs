from src.datetime import time_difference, now, get_hour, get_minute, get_minutes_from_hours
from src.record import lock_vehicle, unlock_vehicle, load_cars, save_cars
from src.fee import get_parking_fee

def main() -> None:
    cars = load_cars()
    while True:
        is_in = None
        is_in = str(input("Parking in? (y|n): "))
        vehicle_number = str(input("Vehicle number: "))

        if is_in == 'y':

            car_in = lock_vehicle(cars, vehicle_number, time=now())

            if not car_in:
                go = str(input("Continue? (y|n): "))
                if go == 'y':
                    continue
                break

            cars[car_in['plate']] = car_in
            print(f"It has been parked at {car_in['time_in']}.")
            go = str(input("Continue? (y|n): "))

            if go == 'y':
                continue
            break

        car_out = unlock_vehicle(cars, vehicle_number, time=now())

        if not car_out:
            go = str(input("Continue? (y|n): "))
            if go == 'y':
                continue
            break
        
        total_hours_parked = time_difference([get_hour(car_out['time_in']), get_hour(car_out['time_out'])], [get_minute(car_out['time_in']), get_minute(car_out['time_out'])])

        print(f"Fee [${get_parking_fee(get_minutes_from_hours(total_hours_parked))}]")
        print(f"It has been parking for {total_hours_parked} hours.")
        print(f"It has been released at {car_out['time_out']}.")

        go = str(input("Continue? (y|n): "))
        if go == 'y':
            continue
        break
    
    save_cars(cars)


if __name__ == "__main__":
    main()