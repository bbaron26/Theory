import time
import matplotlib.pyplot as plt

# Exponential recursion
def determineCombinationLimited(coins, counts, target):
    # If target is 0, we found a combination
    if target == 0:
        return True, []
    
    # If target is negative, it wasn't possible
    if target < 0:
        return False, []
    
    # Go through each coin
    for i in range(len(coins)):
        coin = coins[i]
        
        # Only use coins we have left
        if counts[i] > 0:
            # Reduce the count left for this coin
            counts[i] -= 1
            
            # Recursive call
            result, combination = determineCombinationLimited(coins, counts, target - coin)
            
            # Restore the count of the coin
            counts[i] += 1
            
            # If we reached the target, append the coin to the combination
            if result:
                combination.append(coin)
                return True, combination
            
    # If no combination works, return false
    return False, []

# Coins 
coins = [162, 14, 8, 22]

# 2D array of different sets of counts
countsList = [
    [2, 2, 2, 0],  
    [2, 3, 2, 0],
    [2, 3, 3, 0], 
    [2, 3, 4, 0], 
    [2, 3, 4, 1],
    [2, 3, 4, 2],  
    [2, 3, 5, 2],
    [2, 4, 5, 2],  
    [2, 4, 6, 2]   
]

# Range of targets
targetList = [281, 170, 206, 261, 244]

# Initialize arrays to hold the results
executionTimes = []
results = []
combinations = []
totalCoinsList = []
targetValues = []

# Loop through each set of counts
for counts in countsList:
    # Total coins
    totalCoins = sum(counts) 
    
    # For each totalCoins set, test all targets
    for target in targetList:
        # Start timer
        st = time.time()
        # Determine if the target can be reached with current counts
        result, combination = determineCombinationLimited(coins, counts.copy(), target)
        # End timer
        et = time.time()
	# Calculate total time
        totalTime = et - st
        
        # Store the result, execution time, and combination
        executionTimes.append(totalTime)
        results.append(result)
        totalCoinsList.append(totalCoins)
        #Store target values
        targetValues.append(target)  
        if result:
            combinations.append(combination)
        #Empty list signals no combination
        else:
            combinations.append([])  
        
        # Print results for data
        print(f"Total Coins: {totalCoins}, Target: {target}, Result: {result}, Time: {totalTime:.6f} seconds, Combination: {combination}")

# Plot
plt.figure(figsize=(10, 6))
for i in range(len(totalCoinsList)):
    # Green for successful combination, red for failure
    color = 'g' if results[i] else 'r'  
    plt.scatter(totalCoinsList[i], executionTimes[i], color=color, label=f"Target: {targetValues[i]}" if i == 0 else "")

plt.title('Effect of Total Coins on Execution Time')
plt.xlabel('Total Coins Available')
plt.ylabel('Execution Time (seconds)')
plt.grid(True)
plt.savefig('plot_bbaron2.png')
