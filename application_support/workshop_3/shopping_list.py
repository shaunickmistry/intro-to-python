def main():
    shopping_list = []
    while True:
        item = input("Please give an item for the shopping list: ")
        if item == "END":
            print("You final shopping list is: ", shopping_list)
            break
        shopping_list.append(item)
        print("shopping_list: ", shopping_list)


if __name__ == "__main__":
    main()
