from .controller import OrderManager


def start_application():
    """Provides a menu-driven interface for the staff."""
    manager = OrderManager()

    while True:
        print("\n--- Musical Instrument Order Manager ---")
        print("1. Add a New Order")
        print("2. View All Orders")
        print("3. Update Order Price")
        print("4. Delete an Order")
        print("5. Exit")

        choice = input("Select an option (1-5): ")

        if choice == "1":
            order_id = input("Enter Order ID: ")
            customer = input("Enter Customer Name: ")
            instrument = input("Enter Instrument Name: ")
            price = input("Enter Price: ")
            success, message = manager.add_order(
                order_id, customer, instrument, price
            )
            print(message)

        elif choice == "2":
            orders = manager.get_all_orders()
            if not orders:
                print("No orders found.")
            else:
                print("\n--- Current Orders ---")
                for order in orders:
                    print(order)

        elif choice == "3":
            oid = input("Enter Order ID to update: ")
            price = input("Enter new price: ")
            success, msg = manager.update_order(oid, price)
            print(msg)

        elif choice == "4":
            oid = input("Enter Order ID to delete: ")
            success, msg = manager.delete_order(oid)
            print(msg)

        elif choice == "5":
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
