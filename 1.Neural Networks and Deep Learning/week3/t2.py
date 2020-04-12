import argparse

def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    command1_parser = subparsers.add_parser('command1')
    command1_parser.set_defaults(func=command1)
    command1_parser.add_argument('--name', dest='var')

    command2_parser = subparsers.add_parser('command2')
    command2_parser.set_defaults(func=command2)
    command2_parser.add_argument('--frequency', dest='frequency')

    args = parser.parse_args()
    args.func(args)

def command1(arg):
    # print("command1: %s" % args.nam)
    print("Ciao: " + arg.var)

def command2(args):
    print("comamnd2: %s" % args.frequency)

if __name__ == '__main__':
    main()
