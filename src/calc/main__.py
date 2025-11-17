import argparse
from . import add, sub, mul, div

parser = argparse.ArgumentParser(description="Calc CLI")
parser.add_argument("op", choices=["add", "sub", "mul", "div"])
parser.add_argument("a", type=float)
parser.add_argument("b", type=float)

if __name__ == "__main__":
    args = parser.parse_args()
    ops = {"add": add, "sub": sub, "mul": mul, "div": div}
    print(ops[args.op](args.a, args.b))
