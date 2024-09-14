class Solution:
    def arraySum(self, arr, n):
        total = 0
        for i in range(n):
            total += arr[i]
        return total

# Example usage
sol = Solution()
arr = [1, 2, 3, 4, 5]  # example array
n = len(arr)  # size of array

result = sol.arraySum(arr, n)
print("Sum of elements in array:", result)
