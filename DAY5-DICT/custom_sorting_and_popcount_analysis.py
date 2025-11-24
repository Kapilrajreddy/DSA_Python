if __name__ == "__main__":
    sol = solution()

    arr = [
        [3, 5],
        [1, 2],
        [3, 4],
        [2, 10],
        [1, 9]
    ]

    sol.sortPairs(arr)

    # Print in main only
    for p in arr:
        print(p[0], p[1])

    # Example popcount
    print("Popcount of 15 =", sol.popcount(15))