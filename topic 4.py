class OrderManager:
    def __init__(self, capacity):
        """Initialize the array with a fixed capacity."""
        self.capacity = capacity
        self.orders = [None] * capacity  
        self.count = 0  

    def add_order(self, order):
        """
        Add an order to the array.
        If the array is full, return an error message.
        """
        if self.count < self.capacity:
            self.orders[self.count] = order
            self.count += 1
            return f"Order added: {order}"
        else:
            return "Error: Order list is full!"

    def get_order(self, index):
        """
        Retrieve an order by its index.
        If the index is invalid, return an error message.
        """
        if 0 <= index < self.count:
            return self.orders[index]
        else:
            return "Error: Invalid index!"

    def remove_order(self, index):
        """
        Remove an order by its index.
        Shift subsequent orders to fill the gap.
        """
        if 0 <= index < self.count:
            removed_order = self.orders[index]
            for i in range(index, self.count - 1):
                self.orders[i] = self.orders[i + 1]
            self.orders[self.count - 1] = None
            self.count -= 1
            return f"Order removed: {removed_order}"
        else:
            return "Error: Invalid index!"

    def list_orders(self):
        """List all orders currently in the array."""
        return [order for order in self.orders if order is not None]
if __name__ == "__main__":
    manager = OrderManager(capacity=5)

    print(manager.add_order("Order 1: Website Design"))
    print(manager.add_order("Order 2: Mobile App Development"))
    print(manager.add_order("Order 3: Logo Design"))
    print(manager.add_order("Order 4: SEO Optimization"))
    print(manager.add_order("Order 5: Social Media Marketing"))
    print(manager.add_order("Order 6: Content Writing"))   

    print("\nCurrent Orders:")
    print(manager.list_orders())

    print("\nRetrieve Order at Index 2:")
    print(manager.get_order(2))

    print("\nRemove Order at Index 3:")
    print(manager.remove_order(3))

    print("\nOrders After Removal:")
    print(manager.list_orders())
