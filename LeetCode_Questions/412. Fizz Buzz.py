# Input: n = 3
# Output: ["1","2","Fizz"]

# Input: n = 5
# Output: ["1","2","Fizz","4","Buzz"]

# Input: n = 15
# Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

def fizzBuzz(n):
    """
    :type n: int
    :rtype: List[str]
    """
    ans = []
    for i in range(n):
        j = i+1
        if ((j%3==0) & (j%5==0)):
            ans.append("FizzBuzz")
        elif (j%3==0):
            ans.append("Fizz")
        elif (j%5==0):
            ans.append("Buzz")
        else:
            ans.append(str(i+1))
    return ans

if __name__ == "__main__":
    n=3
    print(fizzBuzz(n))

    n=7
    print(fizzBuzz(n))

    n=15
    print(fizzBuzz(n))
