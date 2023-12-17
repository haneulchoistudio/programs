from datetime import datetime

def _now():
    return datetime.now()

def _time():
    return _now().time()

def _hour():
    return _time().hour

def _minute():
    return _time().minute

def now():
    return f"{_hour()}:{_minute()}"

def get_hour(time: str):
    spt = time.split(":")
    return int(spt[0])
def get_minute(time: str):
    spt = time.split(":")
    return int(spt[1])

def get_minutes_from_hours(hours: int):
    return hours * 60
def get_hours_from_minutes(minutes: int):
    return round(minutes/60, 2)

def time_difference(__hours: list[int], __minutes: list[int]):
    from_h, to_h = __hours
    from_m, to_m = __minutes

    h_d = 0
    m_d = 0

    if from_h > to_h:
        print("Overnight partking not available.")
        return False
    h_d = get_minutes_from_hours(abs(from_h - to_h))
    if from_m > to_m:
        h_d = h_d - 60
        m_d = 60 - (from_m - to_m)
    else:
        m_d = from_m - to_m
    total_d = get_hours_from_minutes(sum([h_d, m_d]))

    return total_d
