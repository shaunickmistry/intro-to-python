import csv


def main():
    with open("demo.csv", newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)


if __name__ == "__main__":
    main()
