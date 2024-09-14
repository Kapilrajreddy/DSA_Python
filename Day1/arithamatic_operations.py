class solution:
    def add(self, a, b):
        return a+b

    def subtract(self, a, b):
        return a-b 

    def multiply(self, a, b):
        return a*b
    
    def divide(self, a, b):
        if b==0:
            return "b should be greater than 0"
        return a//b 

sol = solution()

# Test the methods
print("Addition:", sol.add(10, 5))           # Output: 15
print("Subtraction:", sol.subtract(10, 5))   # Output: 5
print("Multiplication:", sol.multiply(10, 5))# Output: 50
print("Division:", sol.divide(10, 5))        # Output: 2.0
print("Division by zero:", sol.divide(10, 0))