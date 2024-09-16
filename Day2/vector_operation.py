class Solution:
    # Method to add an element to the vector (list)
    def add_to_vector(self, A, x):
        A.append(x)

    # Method to delete an element from the vector (list)
    def delete_element(self, A, element):
        if element in A:
            A.remove(element)
            print("Deleted", element)
        else:
            print("Not found")
    
    # Method to reverse the vector (list)
    def reverse_vector(self, A):
        A.reverse()  # This will reverse the list in-place
    
    # Method to print the size of the vector (list)
    def size_of_vector(self, A):
        print(len(A))
    
    # Method to print all elements of the vector (list)
    def print_vector(self, A):
        print(*A)


# Sample usage of the class methods
sol = Solution()  # Create an instance of the Solution class
A = []  # Empty list to start with

# Input example
commands = [
    ('a', 10),
    ('a', 20),
    ('a', 30),
    ('p',),
    ('r',),
    ('p',),
    ('s',)
]

# Process each command
for command in commands:
    if command[0] == 'a':  # Add element to the vector
        sol.add_to_vector(A, command[1])
    elif command[0] == 'd':  # Delete element from the vector (not in the given sample but can be used)
        sol.delete_element(A, command[1])
    elif command[0] == 'r':  # Reverse the vector
        sol.reverse_vector(A)
    elif command[0] == 'p':  # Print the vector
        sol.print_vector(A)
    elif command[0] == 's':  # Print the size of the vector
        sol.size_of_vector(A)

