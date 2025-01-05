class Node:
    def __init__(self, name, is_product=False, product_details=None):
        self.name = name  # Name of the category or product
        self.is_product = is_product  # Flag to indicate whether the node is a product
        self.product_details = product_details  # Details of the product (if it's a product node)
        self.children = []  # List to store child categories or products

    def add_child(self, child_node):
        self.children.append(child_node)  # Add a child node (subcategory or product)

    def __str__(self):
        return self.name


class Tree:
    def __init__(self, root_name):
        self.root = Node(root_name)  # Create the root of the tree (e.g., Clothing)

    def find_category(self, node, category_name):
        """Recursive function to find a category node by its name"""
        if node.name == category_name:
            return node
        for child in node.children:
            found = self.find_category(child, category_name)
            if found:
                return found
        return None

    def add_category(self, parent_category_name, category_name):
        """Add a new category (subcategory) under a specific parent category"""
        parent_category = self.find_category(self.root, parent_category_name)
        if parent_category:
            new_category = Node(category_name)
            parent_category.add_child(new_category)
            print(f"Category '{category_name}' added under '{parent_category_name}'")
        else:
            print(f"Parent category '{parent_category_name}' not found.")

    def add_product(self, category_name, product_name, product_details):
        """Add a new product under a specific category"""
        category = self.find_category(self.root, category_name)
        if category:
            new_product = Node(product_name, is_product=True, product_details=product_details)
            category.add_child(new_product)
            print(f"Product '{product_name}' added under category '{category_name}'")
        else:
            print(f"Category '{category_name}' not found.")

    def display(self, node, level=0):
        """Recursive function to display the tree in a readable format"""
        print("  " * level + f"- {node.name}")
        if node.is_product:
            print("  " * (level + 1) + f"  (Product Details: {node.product_details})")
        for child in node.children:
            self.display(child, level + 1)

# Example Usage:

def clothing_store_system():
    store_tree = Tree("Clothing Store")  # Root node representing the clothing store

    # Adding categories
    store_tree.add_category("Clothing Store", "Men")
    store_tree.add_category("Clothing Store", "Women")
    store_tree.add_category("Clothing Store", "Accessories")
    
    # Adding subcategories
    store_tree.add_category("Men", "Shirts")
    store_tree.add_category("Men", "Pants")
    store_tree.add_category("Women", "Dresses")
    store_tree.add_category("Women", "Tops")
    
    # Adding products to categories
    store_tree.add_product("Men", "Casual Shirt", "Casual shirt for everyday wear")
    store_tree.add_product("Men", "Formal Shirt", "Formal shirt for office wear")
    store_tree.add_product("Women", "Evening Dress", "Elegant evening dress for parties")
    store_tree.add_product("Women", "Cotton Top", "Comfortable cotton top for summer")

    # Displaying the entire category and product hierarchy
    print("\nClothing Store Hierarchy:")
    store_tree.display(store_tree.root)

# Run the clothing store system simulation
clothing_store_system()
