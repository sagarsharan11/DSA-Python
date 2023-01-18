# Input: s = "00110"
# Output: 1
# Explanation: We flip the last digit to get 00111.

# Input: s = "010110"
# Output: 2
# Explanation: We flip to get 011111, or alternatively 000111.

# Input: s = "00011000"
# Output: 2
# Explanation: We flip to get 00000000.



def minFlipsMonoIncr(s):
    n = len(s)
    cnt0 = s.count('0')
    cnt1 = 0
    res = n - cnt0
    for i in range(n):
        if s[i] == '0':
            cnt0 -= 1
        elif s[i] == '1':
            res = min(res, cnt1 + cnt0)
            cnt1 += 1
    return res







if __name__ == '__main__':
    s = "00110"
    print(minFlipsMonoIncr(s))

    s = "010110"
    print(minFlipsMonoIncr(s))

    s = "00011000"
    print(minFlipsMonoIncr(s))

