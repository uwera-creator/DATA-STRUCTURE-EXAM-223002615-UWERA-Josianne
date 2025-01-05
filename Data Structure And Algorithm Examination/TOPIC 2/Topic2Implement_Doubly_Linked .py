class Node:
    def __init__(self, product):
        self.product = product  # The product (could be an object with name, price, etc.)
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, product):
        new_node = Node(product)
        if self.tail is None:  # List is empty
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def remove(self, product):
        current = self.head
        while current:
            if current.product == product:
                if current.prev:  # Not the first node
                    current.prev.next = current.next
                if current.next:  # Not the last node
                    current.next.prev = current.prev
                if current == self.head:  # Update head if needed
                    self.head = current.next
                if current == self.tail:  # Update tail if needed
                    self.tail = current.prev
                return
            current = current.next

    def display(self):
        current = self.head
        while current:
            print(f"Product: {current.product}")
            current = current.next
        print("\n")

class Deque:
    def __init__(self):
        self.items = []

    def append_front(self, item):
        self.items.insert(0, item)

    def append_back(self, item):
        self.items.append(item)

    def remove_front(self):
        if len(self.items) > 0:
            return self.items.pop(0)
        return None

    def remove_back(self):
        if len(self.items) > 0:
            return self.items.pop()
        return None

    def display(self):
        print("Shopping Cart contents:", self.items)

# Example Usage:
def online_clothing_store():
    # 1. Managing Browsing History with Doubly Linked List
    print("=== Browsing History ===")
    store_history = DoublyLinkedList()

    # Add products to the browsing history list
    store_history.append("Shirt ")
    store_history.append("Jeans ")
    store_history.append("Jacket ")

    # Display the browsing history
    store_history.display()

    # Remove a product from the history (if it was returned or not purchased)
    store_history.remove("Jeans ")

    # Display the updated browsing history
    store_history.display()

    # 2. Managing Shopping Cart with Deque
    print("=== Shopping Cart ===")
    shopping_cart = Deque()

    # Add products to the shopping cart
    shopping_cart.append_back("Shirt ")
    shopping_cart.append_back("Jeans ")
    shopping_cart.append_front("Jacket ")

    # Display the shopping cart
    shopping_cart.display()

    # Remove products from the shopping cart
    shopping_cart.remove_front()  # Remove the first item (Jacket 3)
    shopping_cart.remove_back()   # Remove the last item (Jeans 2)

    # Display the shopping cart after removal
    shopping_cart.display()

# Run the online store example
online_clothing_store()
