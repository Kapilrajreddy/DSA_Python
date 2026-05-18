def addChar(c, s):
    result = c + s + c
    print(result)

if __name__ == "__main__":    
    c = input().strip()
    s = input().strip()
    addChar(c, s)

# Complexity Analysis
# Time Complexity: O(n)  

# Concatenation creates a new string, which requires copying all characters. Here, n is the length of s.
# Space Complexity: O(n) 

# Stores the new string of length n + 2

def addChar(c, s):
    s = list(s)  # Convert string to list for in-place modification
    s.insert(0, c)  # Insert at the beginning
    s.append(c)  # Append at the end
    print("".join(s))  # Convert list back to string and print

if __name__ == "__main__":    
    c = input().strip()
    s = input().strip()
    addChar(c, s)


class solution:
    def addChar(self, c, s):
        return c + s + c

if __name__ == "__main__":
    c = input().strip()
    s = input()
    
    sol = solution()
    result = sol.addChar(c, s)
    
    print(result)
    
# Complexity Analysis
# Time Complexity: O(n)  

# Insertion at the beginning takes O(n), since all characters shift right.

# Appending at the end takes O(1).

# Space Complexity: O(1) / O(n)  

# C++ (Pass by Reference): O(1) (modifies the string in-place).

# Python (String to List Conversion): O(n) (since strings are immutable, a list is used).

# Java (StringBuilder Usage): O(n) (since strings are immutable, StringBuilder is required).

# Overall Space Complexity: O(1) for C++, O(n) for Python & Java.