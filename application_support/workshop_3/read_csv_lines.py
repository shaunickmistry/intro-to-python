def main():
    file = open("demo.csv", "r")
    for line in file.readlines():
        print(line)


if __name__ == "__main__":
    main()
