from collections import defaultdict

# Creating a MultiMap-like structure
multi_map = defaultdict(list)

print(multi_map) #defaultdict(<class 'list'>, {})

# Adding values
multi_map['apple'].append(1)
multi_map['apple'].append(2)
multi_map['banana'].append(3)

print(multi_map) #defaultdict(<class 'list'>, {'apple': [1, 2], 'banana': [3]})