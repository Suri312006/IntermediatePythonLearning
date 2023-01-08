import argparse
import sys


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--x", type=float, default=1.0,
                        help='What is the first number?')
    parser.add_argument("--y", type=float, default=1.0,
                        help='What is the second number?')
    parser.add_argument("--operand", type=str, default="add",
                        help='What operation? (add, sub, mul, div)')

    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))


def calc(args):
    if args.operand == 'add':
        return args.x + args.y
    elif args.operand == 'sub':
        return args.x - args.y
    elif args.operand == 'mul':
        return args.x * args.y
    elif args.operand == 'div':
        return args.x / args.y


if __name__ == '__main__':
    main()

# C:\Users\suri3\PycharmProjects\IntermediatePythonLearning\interpreter\Scripts\python.exe "C:\Users\suri3\PycharmProjects\IntermediatePythonLearning\3. Argparse for CLI.py" -h
