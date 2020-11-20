if __name__ == "__main__":
    order_id = input("Order ID: ")

    if order_id == "123456789":
        print("This order is already cancelled")
    else:
        print("Cancelling order ", order_id)
