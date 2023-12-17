def get_parking_fee(minutes: int, base_minutes = 180, base_cost = 10):
    if minutes < base_minutes:
        return base_cost
    overrate = round(float((minutes - base_minutes)/60), 2)
    cost = base_cost + (base_cost*overrate)
    return cost

    