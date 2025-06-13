def DivideLargeNumber(num1,num2):
    print(f"{(num1/num2):.2f}")
    
def main():
    num1 = int(input())
    num2 = int(input())
    DivideLargeNumber(num1,num2)
    
if __name__=="__main__":
    main()
    
# Complexity Analysis
# Time Complexity: O(1)

# The division operation and printing the result both take constant time.
# Space Complexity: O(1)

# The function uses a constant amount of space for the input values and the result.

                                         