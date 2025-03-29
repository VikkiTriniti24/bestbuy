import products
import store


def start(store_obj):
    while True:
        print("\n  Store Menu")
        print("  ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ")

        if choice == "1":
            print("\nAvailable products:")
            for index, product in enumerate(store_obj.get_all_products(), start=1):
                print(f"{index}. {product}")
        elif choice == "2":
            print(f"Total items in store: {store_obj.get_total_quantity()}")
        elif choice == "3":
            make_order(store_obj)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again!")


def make_order(store_obj):
    products = store_obj.get_all_products()
    order_list = []

    print("\n------")
    for index, product in enumerate(products, start=1):
        print(f"{index}. {product}")
    print("------\n")

    while True:
        choice = input("Which product # do you want? (Enter empty text to finish order): ")
        if choice == "":
            break

        try:
            product_index = int(choice) - 1
            if 0 <= product_index < len(products):
                amount = int(input("What amount do you want? "))
                order_list.append((products[product_index], amount))
                print("Product added to list!\n")
            else:
                print("Invalid product number, try again!\n")
        except ValueError:
            print("Invalid input, please enter a number!\n")

    if order_list:
        total_cost = store_obj.order(order_list)
        print(f"Order placed! Total cost: ${total_cost}")
    else:
        print("No items selected, order cancelled.")


product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250)
]

best_buy = store.Store(product_list)

start(best_buy)

