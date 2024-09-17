class Solution:
    # Method to insert element into the queue
    def insert(self, q, k):
        q.append(k)

    # Method to find frequency of element k
    def findFrequency(self, q, k):
        # Return -1 if the element is not found
        if k not in q:
            return -1
        return q.count(k)


# Input details
N = 8  
elements_to_insert = [1, 2, 3, 4, 5, 2, 3, 1]  # Elements to insert
M = 5  
elements_to_find = [1, 3, 2, 9, 10]  # Elements to find frequency

# Create the queue
queue = []

# Create an instance of the solution class
sol = Solution()

# Insert elements into the queue
for elem in elements_to_insert:
    sol.insert(queue, elem)

# Find the frequency of each element in the list to find
for elem in elements_to_find:
    frequency = sol.findFrequency(queue, elem)
    print(f"Frequency of {elem}: {frequency}")
