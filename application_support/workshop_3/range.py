import sys


def main(start, stop):
    for x in range(start, stop):
        if x % 2 == 0:
            print(x)


if __name__ == "__main__":
    if sys.argv > 2:
        args = sys.argv
        main(args[0], args[1])
    else:
        start = int(input("Start: "))
        stop = int(input("Stop: "))
        main(start, stop)
