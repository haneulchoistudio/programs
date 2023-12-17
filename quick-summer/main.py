import sys
from src.args import args
from src.sums import sums

def print_args_one_by_one(*argvs: str):
    print("Numerics Passed")
    for numeric in argvs:
        print(f"-> {numeric}")
def print_result(total: float):
    print("Result")
    print(f"-> {total}")

def main() -> None:

    argvs = args(*sys.argv[1:])    

    if not argvs:
        return
    
    print_args_one_by_one()

    total = sums("0", *argvs)

    print_result(total)

if __name__ ==  "__main__":
    main()