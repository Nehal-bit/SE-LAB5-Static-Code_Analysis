import json
from datetime import datetime


class InventorySystem:

    def __init__(self):
        """Initialize a new empty stock dictionary."""
        self.stock_data = {}

    def add_item(self, item="default", qty=0, logs=None):
        """Add quantity of an item to the stock."""
        if logs is None:
            logs = []
        if not isinstance(item, str) or not isinstance(qty, (int, float)):
            print("Invalid item name or quantity type.")
            return
        self.stock_data[item] = self.stock_data.get(item, 0) + qty
        logs.append(f"{datetime.now()}: Added {qty} of {item}")

    def remove_item(self, item, qty):
        """Remove quantity of an item from the stock."""
        try:
            if item in self.stock_data:
                self.stock_data[item] -= qty
                if self.stock_data[item] <= 0:
                    del self.stock_data[item]
            else:
                print(f"Item '{item}' not found.")
        except (KeyError, TypeError) as e:
            print(f"Error while removing item: {e}")

    def get_qty(self, item):
        """Return the quantity of an item, or 0 if it does not exist."""
        return self.stock_data.get(item, 0)

    def load_data(self, file="inventory.json"):
        """Load stock data from a JSON file."""
        try:
            with open(file, "r", encoding="utf-8") as f:
                self.stock_data = json.load(f)
        except FileNotFoundError:
            print("No existing inventory file found. Starting fresh.")
            self.stock_data = {}
        except json.JSONDecodeError:
            print("Error decoding JSON file. Starting with empty inventory.")
            self.stock_data = {}

    def save_data(self, file="inventory.json"):
        """Save current stock data to a JSON file."""
        with open(file, "w", encoding="utf-8") as f:
            json.dump(self.stock_data, f, indent=4)

    def print_data(self):
        """Print a simple report of all items in stock."""
        print("Items Report:")
        for item, qty in self.stock_data.items():
            print(f"{item} -> {qty}")

    def check_low_items(self, threshold=5):
        """Return a list of items below the given threshold."""
        return [i for i, q in self.stock_data.items() if q < threshold]


def main():
    """Main function to demonstrate inventory operations."""
    inventory = InventorySystem()

    inventory.add_item("apple", 10)
    inventory.add_item("banana", 2)
    inventory.add_item("orange", 1)

    inventory.remove_item("apple", 3)
    inventory.remove_item("grape", 1)

    print(f"Apple stock: {inventory.get_qty('apple')}")
    print(f"Low items: {inventory.check_low_items()}")

    inventory.save_data()
    inventory.load_data()
    inventory.print_data()


if __name__ == "__main__":
    main()
