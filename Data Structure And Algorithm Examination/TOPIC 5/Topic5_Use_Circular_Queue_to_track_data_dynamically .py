class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size  # Initialize the queue with None values
        self.front = self.rear = -1  # Both pointers start off at -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, item):
        """Add a new user to the queue (virtual fitting room)"""
        if self.is_full():
            print("Queue is full. Overwriting the oldest user...")
            self.dequeue()  # Remove the oldest user if the queue is full
        if self.is_empty():
            self.front = self.rear = 0  # Set the front and rear to 0 if the queue was empty
        else:
            self.rear = (self.rear + 1) % self.size  # Move the rear pointer circularly
        self.queue[self.rear] = item
        print(f"User {item} added to the queue.")

    def dequeue(self):
        """Remove the front user from the queue"""
        if self.is_empty():
            print("Queue is empty. No users to dequeue.")
            return None
        removed_user = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1  # Reset the queue if it becomes empty
        else:
            self.front = (self.front + 1) % self.size  # Move the front pointer circularly
        return removed_user

    def peek(self):
        """Peek at the front of the queue (next user to be processed)"""
        if self.is_empty():
            print("Queue is empty.")
            return None
        return self.queue[self.front]

    def display(self):
        """Display all users in the queue"""
        if self.is_empty():
            print("Queue is empty.")
            return
        index = self.front
        print("Virtual Fitting Room Queue: ", end="")
        while True:
            print(self.queue[index], end=" ")
            if index == self.rear:
                break
            index = (index + 1) % self.size
        print()

# Example Usage:
def virtual_fitting_room():
    fitting_room_queue = CircularQueue(size=5)

    # Enqueue users into the virtual fitting room queue
    fitting_room_queue.enqueue("User 1")
    fitting_room_queue.enqueue("User 2")
    fitting_room_queue.enqueue("User 3")
    fitting_room_queue.enqueue("User 4")
    fitting_room_queue.enqueue("User 5")

    # Display the queue after all users are added
    fitting_room_queue.display()

    # Adding a new user when the queue is full (will overwrite the oldest user)
    fitting_room_queue.enqueue("User 6")

    # Display the queue after adding User 6
    fitting_room_queue.display()

    # Dequeue users (process users in the queue)
    fitting_room_queue.dequeue()  # Remove User 2
    fitting_room_queue.dequeue()  # Remove User 3
    fitting_room_queue.display()  # Show remaining users in the queue

    # Add new users after some have been dequeued
    fitting_room_queue.enqueue("User 7")
    fitting_room_queue.enqueue("User 8")
    fitting_room_queue.display()

# Run the virtual fitting room simulation
virtual_fitting_room()
