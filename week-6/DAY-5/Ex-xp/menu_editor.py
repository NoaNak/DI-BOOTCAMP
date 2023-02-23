from index import MenuItem, run_query

def load_manager(name, price):
    return MenuItem(name, price)
    
def show_user_menu():
    out = """
    (1) To add a new item 
    (2) To remove an item
    (3) To show restaurant menu
    (4) To Exit program

    """
    print (out)

    choice = input("Choose an option: ")

    if choice == "1":
        add_item_to_menu()
    elif choice == "2":
        remove_item_from_menu()
    elif choice == "3":
        show_restaurant_menu()
        show_user_menu()
    elif choice == "4":
        show_restaurant_menu()
        exit()
    else:
        print("Invalid choice.")
        show_user_menu()

    def add_item_to_menu():
        name = input("Enter item name: ")
        price = input("Enter item price: ")
        item_added = False
        for item in MenuItem:
            if item.add_item(name, price):
                item_added = True
                break
        if item_added:
            print("Item was added successfully.")
        else:
            print("There was an error adding the item.")

    def remove_item_from_menu():
        name = input("Enter item name: ")
        item_removed = False

        for item in MenuItem:
            if item.remove_item(name):
                item_removed = True
            break

        if item_removed:
            print("Item was removed successfully.")
        else:
            print("There was an error removing the item.")

    def show_restaurant_menu():
        print("Restaurant Menu:")

    for item in MenuItem:
        print(item.get_item())

load_manager()
show_user_menu()