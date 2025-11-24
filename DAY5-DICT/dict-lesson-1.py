# Sample Python code demonstrating dictionary usage
my_dict = {1: 3, 2: 5, 3: 8}

my_dict[4] = 9  # Adding a new key-value pair
my_dict[3] = 7  # Updating the value associated with key 3

for key, value in my_dict.items():
    print(key, value)

print(my_dict.get(4))  # Returns 9
print(my_dict.get(10, "Not Found"))  # Returns 'Not Found' as 10 is not a key in the dictionary

# Checking if a key exists in the dictionary
if 2 in my_dict:
    print("Found:", my_dict[2])