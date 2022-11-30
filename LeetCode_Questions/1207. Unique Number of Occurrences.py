# Input: arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

# Input: arr = [1,2]
# Output: false


def uniqueOccurrences(arr):
    val_dict = dict()
    for i in range(len(arr)):
        if arr[i] not in val_dict:
            val_dict.update({arr[i]:1})
        elif arr[i] in val_dict:
            counter = val_dict[arr[i]] + 1
            val_dict.update({arr[i]:counter})
    if len(set(val_dict.keys())) == len(set(val_dict.values())):
        return True
    else:
        return False
    

if __name__ == "__main__":
    arr = [1,2,2,1,1,3]
    print(uniqueOccurrences(arr))

    arr = [1,2]
    print(uniqueOccurrences(arr))