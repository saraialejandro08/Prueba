from bisect import bisect_right

# Input reading
n = int(input())
prices = list(map(int, input().split()))
q = int(input())
queries = [int(input()) for _ in range(q)]

# Step 1: Sort the prices
prices.sort()

# Step 2: Answer each query using binary search
results = []
for m in queries:
    # Find the number of shops where price <= m
    count = bisect_right(prices, m)
    results.append(count)

# Output the results
print("\n".join(map(str, results)))
