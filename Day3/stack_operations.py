class Solution:
    
    def __init__(self):
        # Initialize mini to infinity for tracking minimum element
        self.mini = float('inf')
    
    # Push an element to the stack
    def push(self, arr, ele):
        if len(arr) == 0:
            arr.append(ele)
            self.mini = ele
        else:
            if ele < self.mini:
                arr.append(2 * ele - self.mini)
                self.mini = ele
            else:
                arr.append(ele)
    
    # Pop an element from the stack
    def pop(self, arr):
        if len(arr) == 0:
            return None  # Handle empty stack case
        top = arr[-1]
        if top < self.mini:
            # This means the popped element is a modified value
            self.mini = 2 * self.mini - top
        arr.pop()
    
    # Check if the stack is empty
    def isEmpty(self, arr):
        return len(arr) == 0
    
    # Get the minimum element in the stack
    def getMin(self, arr):
        if len(arr) == 0:
            return None  # Handle empty stack case
        return self.mini

# Driver code to demonstrate functionality
if __name__ == "__main__":
    s = Solution()
    arr = []
    
    s.push(arr, 18)
    s.push(arr, 19)
    s.push(arr, 29)
    s.push(arr, 1)
    
    print("Minimum:", s.getMin(arr))  # Should print 1
    
    s.pop(arr)  # Removes 1
    print("Minimum after pop:", s.getMin(arr))  # Should print 18
