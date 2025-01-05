class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Adds an item to the queue."""
        self.items.append(item)

    def dequeue(self):
        """Removes an item from the queue."""
        return self.items.pop(0) if self.items else None

    def peek(self):
        """Returns the first item in the queue without removing it."""
        return self.items[0] if self.items else None

    def is_empty(self):
        """Checks if the queue is empty."""
        return len(self.items) == 0

    def size(self):
        """Returns the size of the queue."""
        return len(self.items)

    def display(self):
        """Displays all items in the queue."""
        print("Queue:", self.items)

# Example usage in the online clothing store context:
def virtual_fitting_room_processing():
    fitting_room_queue = Queue()

    # Enqueue users into the virtual fitting room processing queue
    fitting_room_queue.enqueue("Uwera")
    fitting_room_queue.enqueue("Jemimah")
    fitting_room_queue.enqueue("Djamillah")
    
    # Display the current queue
    print("Virtual Fitting Room Queue:")
    fitting_room_queue.display()
    
    # Process the users in the queue (First Come, First Serve)
    while not fitting_room_queue.is_empty():
        user = fitting_room_queue.dequeue()
        print(f"Processing {user} in the virtual fitting room...")
    
    # Display queue after processing
    print("\nAfter processing all users:")
    fitting_room_queue.display()

# Run the virtual fitting room processing example
virtual_fitting_room_processing()

