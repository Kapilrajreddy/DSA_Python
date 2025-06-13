def multiDivision(num1,num2):
    print(f"{(num1*num2):.2f}")
    if(num2==0):
        print("Undefined")
    else:
        print(f"{(num1/num2):.2f}")
    
    
    
def main():
    num1,num2 = list(map(float,input().split()))
    multiDivision(num1,num2)
        
if __name__ == "__main__":
    main()
    
# Complexity Analysis
# Time Complexity: O(1)  

# The operations performed (multiplication, division, and a conditional check) are constant-time arithmetic operations.
# Space Complexity: O(1)  

# No extra space is used, as the function directly prints the output.
