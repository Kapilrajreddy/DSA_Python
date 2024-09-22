# User function Template for python3
class Solution:
    
    # Function to insert element into the set
    def insert(self, s, x):
        # Inserts an element x to the set s.
        s.add(x)
    
    # Function to print contents of the set
    def print_contents(self, s):
        # Prints the contents of the set s in sorted order.
        for u in sorted(s):
            print(u, end=" ")
        print()  # For a new line after printing the set contents
    
    # Function to erase element from the set
    def erase(self, s, x):
        # Erases an element x from the set s.
        s.discard(x)
    
    # Function to find if an element exists in the set
    def find(self, s, x):
        # Returns 1 if the element x is present in set s else returns -1.
        return "1" if x in s else "-1"
    
    # Function to return the size of the set
    def size(self, s):
        # Returns the size of the set s.
        return len(s)

# Driver code
if __name__ == "__main__":
    solution = Solution()
    s = set()  # Initialize an empty set
    q = 6  # Number of queries (based on the example)
    
    # Example queries (as per the provided format)
    Queries = [
        "a 1",  # Add 1 to the set
        "a 3",  # Add 3 to the set
        "b",    # Print contents of the set
        "c 2",  # Check if 2 is in the set
        "a 2",  # Add 2 to the set
        "b"     # Print contents of the set
    ]
    
    # Processing the queries
    for query in Queries:
        parts = query.split()
        if parts[0] == 'a':  # Insert operation
            x = int(parts[1])
            solution.insert(s, x)
        elif parts[0] == 'b':  # Print contents of the set
            solution.print_contents(s)
        elif parts[0] == 'c':  # Find element in the set
            x = int(parts[1])
            print(solution.find(s, x))

