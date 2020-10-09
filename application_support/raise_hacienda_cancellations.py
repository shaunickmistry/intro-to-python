import requests
import csv
import datetime
import json


base_url = "cancellation-test.made.com"


def raise_cancel_item_to_hacienda_stream(order_id, order_item_id, sku, datetime):
    payload = {
        "order_id": order_id,
        "order_item_id": order_item_id,
        "sku": sku,
        "requested_datetime": datetime
    }

    payload = json.dumps(payload)
    print('Invoking the following: ', payload, '\n')
    response = requests.post(f'https://{base_url}/cancel', data=payload)
    print(response.status_code)


def read_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            raise_cancel_item_to_hacienda_stream(
                row['order_reference'],
                row['order_item_id'],
                row['product_sku'],
                datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
            )


if __name__ == "__main__":
    filepath = "hacienda_cancellation_requests.csv"
    read_csv(filepath)
