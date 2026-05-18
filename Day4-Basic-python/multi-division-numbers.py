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

def computeResults(num1, num2):
    result = [f"{num1 * num2:.2f}"]

    if num2 != 0:
        result.append(f"{num1 / num2:.2f}")
    else:
        result.append("Undefined")

    return result

if __name__ == "__main__":
    num1, num2 = map(float, input().split())

    result = computeResults(num1, num2)

    for value in result:
        print(value)                                       
    
# Complexity Analysis
# Time Complexity: O(1)  

# The operations performed (multiplication, division, and a conditional check) are constant-time arithmetic operations.
# Space Complexity: O(1)  

# No extra space is used, as the function directly prints the output.
