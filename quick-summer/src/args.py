def args(*argvs: str):
    for i, arg in enumerate(argvs):
        try:
            float(arg)
        except ValueError:
            return _when_float_fails()
        parsed_length = _parse_decimal_points(arg)
        if parsed_length:
            return _when_decimal_limit_exceeds()                
    return argvs

def _parse_decimal_points(value: str):
    v = value.split(".")
    length_2 = len(v) == 2
    length_arg1_2 = len(v[1]) > 2 if length_2 else False 
    return length_2, length_arg1_2

def _when_float_fails():
    print(f"You entered non-numeric value to the terminal at.")
    print(f"-> WHERE: INDEX [{i}], VALUE [{arg}]")    
    return False  
def _when_decimal_limit_exceeds():
    print(f"You entered numeric value over 2 decimal points. Only allowed to 2 decimal points.")
    print(f"-> WHERE: INDEX [{i}], VALUE [{arg}]")    
    return False     