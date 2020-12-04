import csv


def cancel(order_id):
    pass

def main():
    with open("demo.csv", newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["status"] == "Cancelled":
                cancel(row["order_id"])
            print(row)


if __name__ == "__main__":
    main()
