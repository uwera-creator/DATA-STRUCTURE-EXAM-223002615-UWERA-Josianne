class Node:
    def __init__(self, order_id, order_data):
        self.order_id = order_id
        self.order_data = order_data  # Additional data like items, total price, etc.
        self.left = None
        self.right = None
        self.height = 1  # Height of node (for balancing)

class AVLTree:
    def __init__(self, max_orders):
        self.root = None
        self.max_orders = max_orders  # Fixed number of orders to maintain

    def height(self, node):
        return node.height if node else 0

    def update_height(self, node):
        node.height = max(self.height(node.left), self.height(node.right)) + 1

    def balance_factor(self, node):
        return self.height(node.left) - self.height(node.right)

    def rotate_left(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        self.update_height(z)
        self.update_height(y)
        return y

    def rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        self.update_height(y)
        self.update_height(x)
        return x

    def balance(self, node):
        balance = self.balance_factor(node)
        if balance > 1:
            if self.balance_factor(node.left) < 0:
                node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if balance < -1:
            if self.balance_factor(node.right) > 0:
                node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        return node

    def insert(self, node, order_id, order_data):
        if not node:
            return Node(order_id, order_data)
        
        if order_id < node.order_id:
            node.left = self.insert(node.left, order_id, order_data)
        else:
            node.right = self.insert(node.right, order_id, order_data)

        self.update_height(node)
        return self.balance(node)

    def add_order(self, order_id, order_data):
        self.root = self.insert(self.root, order_id, order_data)
        self.ensure_order_limit()

    def ensure_order_limit(self):
        """Ensure the AVL Tree doesn't exceed the maximum order limit"""
        if self.get_size(self.root) > self.max_orders:
            # Delete the smallest (leftmost) node (or based on other logic)
            self.root = self.delete_node(self.root, self.find_min(self.root).order_id)

    def find_min(self, node):
        """Find the minimum value node (smallest order_id)"""
        current = node
        while current.left:
            current = current.left
        return current

    def get_size(self, node):
        """Get the size of the tree (number of nodes)"""
        if not node:
            return 0
        return 1 + self.get_size(node.left) + self.get_size(node.right)

    def delete_node(self, node, order_id):
        """Deletes a node with a specific order_id"""
        if not node:
            return node
        
        if order_id < node.order_id:
            node.left = self.delete_node(node.left, order_id)
        elif order_id > node.order_id:
            node.right = self.delete_node(node.right, order_id)
        else:
            # Node with the order_id is found
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            temp = self.find_min(node.right)
            node.order_id, node.order_data = temp.order_id, temp.order_data
            node.right = self.delete_node(node.right, temp.order_id)

        self.update_height(node)
        return self.balance(node)

    def display_in_order(self, node):
        """In-order traversal to display all orders in the AVL tree"""
        if node:
            self.display_in_order(node.left)
            print(f"Order ID: {node.order_id}, Order Data: {node.order_data}")
            self.display_in_order(node.right)

    def display_orders(self):
        """Displays all orders in the AVL tree in sorted order"""
        self.display_in_order(self.root)

# Example Usage:
def order_management_system():
    # Initialize AVL Tree to manage up to 5 order
    order_tree = AVLTree(max_orders=5)

    # Add orders
    order_tree.add_order(3, "Order 3 details")
    order_tree.add_order(1, "Order 1 details")
    order_tree.add_order(4, "Order 4 details")
    order_tree.add_order(5, "Order 5 details")
    order_tree.add_order(2, "Order 2 details")

    print("Orders in the AVL tree after insertion:")
    order_tree.display_orders()

    # Add one more order, which will cause the smallest order (Order ID 1) to be deleted
    order_tree.add_order(6, "Order 6 details")

    print("\nOrders after adding the 6th order (Order ID 1 should be deleted):")
    order_tree.display_orders()

# Run the order management example
order_management_system()
