def cancel_order(order_id):
    if order_id == "123":
        print("This order is already cancelled")
    else:
        print("Cancelling order ", order_id)


if __name__ == "__main__":
    order_id = input("Order ID: ")
    cancel_order(order_id)
