# 🎯 Challenge
# - Create an inventory system tracking items and quantities with a dictionary

inventory = { "item1": 10, "item2": 5, "item3": 20 }
def add_item(item, quantity):
    """Add an item with its quantity to the inventory."""
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity
def remove_item(item, quantity):
    """Remove a specified quantity of an item from the inventory."""
    if item in inventory and inventory[item] >= quantity:
        inventory[item] -= quantity
        if inventory[item] == 0:
            del inventory[item]
    else:
        print(f"Cannot remove {quantity} of {item}. Not enough stock or item does not exist.")
def get_inventory():
    """Return the current inventory."""
    return inventory
def display_inventory():
    """Display the current inventory in a readable format."""
    print("Current Inventory:")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")
# Example usage
add_item("item4", 15)
remove_item("item2", 3)
display_inventory()
# Output the current inventory
print(get_inventory())
