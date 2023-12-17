def sums(__total: str = "0", *args: list[str]) -> float:
    num_total = float(__total)
    if len(args) == 0:
        return _round_to_tenth(num_total)
    num_total = num_total + float(args[0])
    num_total = str(num_total)
    return sum(num_total, *args[1:])

def _round_to_tenth(value: float) -> float:
    return round(value, 2)