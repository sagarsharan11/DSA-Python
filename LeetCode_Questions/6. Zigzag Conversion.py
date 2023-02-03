# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"

# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I

# Input: s = "A", numRows = 1
# Output: "A"


def convert(s, numRows):
    if numRows == 1: 
        return s
    rows = [""] * numRows
    backward = True
    index = 0
    for char in s:
        rows[index] += char
        if index == 0 or index == numRows - 1:
            backward = not backward
        if backward:
            index -= 1
        else:
            index += 1
    return "".join(rows)

if __name__=="__main__":
    s = "PAYPALISHIRING"
    numRows = 3
    print(convert(s, numRows))