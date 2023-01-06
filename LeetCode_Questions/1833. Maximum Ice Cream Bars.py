# Input: costs = [1,3,2,4,1], coins = 7
# Output: 4
# Explanation: The boy can buy ice cream bars at indices 0,1,2,4 for a total price of 1 + 3 + 2 + 1 = 7.

# Input: costs = [10,6,8,7,7,8], coins = 5
# Output: 0
# Explanation: The boy cannot afford any of the ice cream bars.

# Input: costs = [1,6,3,1,2,5], coins = 20
# Output: 6
# Explanation: The boy can buy all the ice cream bars for a total price of 1 + 6 + 3 + 1 + 2 + 5 = 18.

"""
Total Cases:
1. Cannot buy any ice-cream
2. Can buy all the ice-cream
3. what if the ice-creame cost > coins
"""

def maxIceCream(costs, coins):
    s = 0
    costs.sort()
    idx = 0
    while idx < len(costs):
        if s == coins:
            return idx
        elif s < coins:
            s += costs[idx]
        elif s > coins:
            return idx - 1
        idx += 1
    if s < coins:
        return len(costs)
    elif s > coins:
        return len(costs) - 1 

## Time Complexity - O(nlogn + n) | nlogn - sorting list & n - while loop


### More Optimal Way ::::----
# def maxIceCream(costs, coins):
#     s = 0
#     counter = 0
#     for idx in range(len(costs)):
#         if s == coins:
#             # count += 1
#             print("Sum:", s)
#             return counter
#         elif (s < coins):
#             if (s + costs[idx] <= coins):
#                 s += costs[idx]
#                 counter += 1
#     print("Sum:", s)
#     return counter


if __name__ == "__main__":
    # costs = [1,3,2,4,1]
    # coins = 7
    # print(maxIceCream(costs, coins))

    # costs = [10,6,8,7,7,8]
    # coins = 5
    # print(maxIceCream(costs, coins))

    # costs = [1,6,3,1,2,5]
    # coins = 20
    # print(maxIceCream(costs, coins))

    # costs = [7,3,3,6,6,6,10,5,9,2]
    # coins = 56
    # print(maxIceCream(costs, coins))

    # costs = [4,7,6,4,4,2,2,4,8,8]
    # coins = 41
    # print(maxIceCream(costs, coins))

    costs = [27,23,33,26,46,86,70,85,89,82,57,66,42,18,18,5,46,56,42,82,52,78,4,27,96,74,74,52,2,24,78,18,42,10,12,10,80,30,60,38,32,7,98,26,18,62,50,42,15,14,32,86,93,98,47,46,58,42,74,69,51,53,58,40,66,46,65,2,10,82,94,26,6,78,2,101,97,16,12,18,71,5,46,22,58,12,18,62,61,51,2,18,34,12,36,58,20,12,17,70]
    coins = 241
    print(maxIceCream(costs, coins))
