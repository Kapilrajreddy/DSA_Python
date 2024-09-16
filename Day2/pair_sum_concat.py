def solution(pairs):
    total = 0 
    sent = "" 
    
    # Iterate over each pair in the list of tuples
    for i in pairs:
        total += i[0]  # Add the first element of the tuple to the total
        sent += i[1]  # Concatenate the second element of the tuple to the string 'sent'
    
    # Output the results
    print(total)
    print(sent)
    print(len(sent))

# Sample input
pairs = [
    (5, 'code'),
    (15, 'challenge'),
    (25, 'is'),
    (10, 'fun')
]

# Calling the function with the sample input
solution(pairs)
