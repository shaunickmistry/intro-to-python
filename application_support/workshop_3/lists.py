def main():
    shopping_list = ["Apples", "Milk", "Bread"]
    # ["Apples", "Milk", "Bread", "Bananas"]
    shopping_list.append("Bananas")
    shopping_list.remove("Apples")
    shopping_list.count()
    shopping_list[0] = "Newspaper"


if __name__ == "__main__":
    main()
