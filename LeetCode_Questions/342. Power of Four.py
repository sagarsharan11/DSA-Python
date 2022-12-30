# Input: n = 16
# Output: true

# Input: n = 5
# Output: false

# Input: n = 1
# Output: true



def isPowerOfFour(n):
    newN = n%4
    if (newN == 0) or (n == 1):
        return True
    elif (newN >= 1) and (newN < 4) :
        return False
    isPowerOfFour(newN)


if __name__ == "__main__":
    n = 16
    print(isPowerOfFour(n))

    n = 1
    print(isPowerOfFour(n))

    n = -2147483648
    print(isPowerOfFour(n))

    n = 5
    print(isPowerOfFour(n))