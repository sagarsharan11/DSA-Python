# Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
# Output: 3
# Explanation:
# Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
# Travel to station 4. Your tank = 4 - 1 + 5 = 8
# Travel to station 0. Your tank = 8 - 2 + 1 = 7
# Travel to station 1. Your tank = 7 - 3 + 2 = 6
# Travel to station 2. Your tank = 6 - 4 + 3 = 5
# Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
# Therefore, return 3 as the starting index.


# Input: gas = [2,3,4], cost = [3,4,3]
# Output: -1
# Explanation:
# You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
# Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
# Travel to station 0. Your tank = 4 - 3 + 2 = 3
# Travel to station 1. Your tank = 3 - 3 + 3 = 3
# You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
# Therefore, you can't travel around the circuit once no matter where you start.


### gas = amount of gas at ith station
### cost = cost to travel from ith to (i+1)th


"""
1. Start from the index which has more gas than required to travel to next station
2. Loop back again to the same starting index and keep that index stored | create a loop in that way
3. If cannot travel back to same index then return -1
4. If fuel ends in between handel it seperately, there always exists a uniqe solution
"""


def canCompleteCircuit(gas, cost):
    tank = 0
    diff = 0
    pos = []
    idx = 0
    while idx < len(cost):
        ## if circuit is completed
        if idx in pos:
            break
        
        ## if gas at station is more than gas req to travel next station
        if cost[idx] <= gas[idx] + diff:
            pos.append(idx)
            diff = gas[idx] - cost[idx]
            # if len(pos) == 1:
            #     tank =  gas[idx]
            #     idx += 1
            # else:
            #     tank += tank + gas[idx] - cost[idx-1]
            #     idx += 1
            
            if idx == len(cost) - 1:
                idx = 0
        idx += 1
    if len(pos) == len(cost):
        return pos[0]
    else:
        return -1



#### Optimal Approach
# def canCompleteCircuit(gas, cost):
#     n, total_surplus, surplus, start = len(gas), 0, 0, 0
        
#     for i in range(n):
#         total_surplus += gas[i] - cost[i]
#         surplus += gas[i] - cost[i]
#         if surplus < 0:
#             surplus = 0
#             start = i + 1
#     return -1 if (total_surplus < 0) else start



if __name__ == "__main__":
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    print(canCompleteCircuit(gas, cost))

    gas = [2,3,4]
    cost = [3,4,3]
    print(canCompleteCircuit(gas, cost))