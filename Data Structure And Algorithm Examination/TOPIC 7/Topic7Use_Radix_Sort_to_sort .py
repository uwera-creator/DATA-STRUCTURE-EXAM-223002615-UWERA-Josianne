def counting_sort(arr, exp):
    """A stable counting sort algorithm to sort the array based on the digit represented by exp"""
    n = len(arr)
    output = [0] * n  # Output array
    count = [0] * 10  # Counting array for digits 0-9
    
    # Store count of occurrences in count[]
    for i in range(n):
        index = arr[i] // exp % 10
        count[index] += 1
    
    # Change count[i] so that count[i] now contains the actual position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # Build the output array using the count array
    for i in range(n - 1, -1, -1):
        index = arr[i] // exp % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
    
    # Copy the sorted output array to arr[], so that arr[] now contains sorted numbers
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    """The main function to implement Radix Sort"""
    # Find the maximum number to know the number of digits
    max_val = max(arr)
    
    # Perform counting sort for every digit. Note that the exp (10^i) is passed.
    exp = 1
    while max_val // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# Example usage for the online clothing store with virtual fitting room data:
def virtual_fitting_room_priority_sort():
    # Example data: [priority_number, user_id]
    users = [
        (5, "User001"),  # User with priority 5
        (1, "User003"),  # User with priority 1
        (3, "User002"),  # User with priority 3
        (2, "User004"),  # User with priority 2
        (4, "User005")   # User with priority 4
    ]
    
    # Extract the priority numbers for sorting
    priorities = [user[0] for user in users]
    
    # Apply Radix Sort on the priority numbers
    radix_sort(priorities)
    
    # After sorting, display the users in priority order
    print("Sorted Users based on Priority:")
    for priority in priorities:
        # Find the corresponding user ID for each sorted priority
        user = next(user for user in users if user[0] == priority)
        print(f"User ID: {user[1]}, Priority: {user[0]}")

# Run the virtual fitting room priority sort
virtual_fitting_room_priority_sort()
