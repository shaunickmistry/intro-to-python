import csv
import sys


def order_in_state(filename="demo_read.csv", status="Cancelled"):
    with open("demo_output.csv", mode="w", newline='') as output_file:
        with open(filename, newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                if row["status"] == status:
                    writer = csv.writer(output_file)
                    writer.writerow(row)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        status = sys.argv[2]
        order_in_state(filename, status)
    else:
        order_in_state()
