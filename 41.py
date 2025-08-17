def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0]*(capacity+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for w in range(capacity+1):
            if weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][capacity]

if __name__ == "__main__":
    weights = list(map(int, input("Enter weights separated by space: ").split()))
    values = list(map(int, input("Enter values separated by space: ").split()))
    capacity = int(input("Enter maximum capacity: "))
    print("Maximum value that can be carried:", knapsack(weights, values, capacity))
