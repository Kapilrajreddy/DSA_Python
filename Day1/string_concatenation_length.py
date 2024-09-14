def solution(n, arr):
    new_string = "".join(arr)
    return len(new_string) 
# Example usage
n = 5
arr = ['a', 'bc', 'def', 'gh', 'i']  # example array of strings
result = solution(n, arr)

print("Length of the concatenated string:", result)
