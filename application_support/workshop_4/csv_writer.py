import csv


def main():
    with open("demo.csv", "w") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["order_id", "status"])
        writer.writerow(["123", "Cancelled"])


if __name__ == "__main__":
    main()
