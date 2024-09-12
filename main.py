def print_bill(name, items):
    """
    Print a detailed bill including item names and their prices.

    Parameters:
    name (str): The name of the customer.
    items (dict): A dictionary where keys are item names and values are their prices.
    """
    total = sum(items.values())
    print(f"\n{name}'s Bill:")
    for item, price in items.items():
        print(f"{item}: ${price:.2f}")
    print(f"Total: ${total:.2f}")
    print("Thank you for shopping with us!")

def display_items(items):
    """
    Display a list of items and their prices.

    Parameters:
    items (dict): A dictionary where keys are item names and values are their prices.
    """
    if not items:
        print("No items have been added yet.")
        return

    print("\nCurrent items in your cart:")
    for item, price in items.items():
        print(f"{item}: ${price:.2f}")

def main():
    """
    Main function to add items and print the final bill.
    """
    items = {}

    while True:
        action = input("Enter 'a' to add an item, 'd' to display items, or 'q' to quit:\n")
        
        if action.lower() == 'q':
            customer_name = input("Enter your name:\n")
            print_bill(customer_name, items)
            break
        elif action.lower() == 'a':
            item_name = input("Enter the item name:\n")
            user_input = input(f"Enter the price for '{item_name}':\n")
            
            try:
                price = float(user_input)  
                if price < 0:
                    print("Price cannot be negative. Please enter a valid amount.")
                    continue
                items[item_name] = price
                print(f"Added '{item_name}' with price ${price:.2f}.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif action.lower() == 'd':
            display_items(items)
        else:
            print("Invalid action. Please enter 'a' to add an item, 'd' to display items, or 'q' to quit.")

if __name__ == "__main__":
    main()
