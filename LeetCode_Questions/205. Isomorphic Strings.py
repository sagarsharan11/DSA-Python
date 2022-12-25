# Input: s = "egg", t = "add"
# Output: true

# Input: s = "foo", t = "bar"
# Output: false

# Input: s = "paper", t = "title"
# Output: true



def isIsomorphic(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """

    d = {}
    value_set = set()

    for idx, val in enumerate(s):
        try:
            if d[val] != t[idx]:
                return False
        except:
            d[val] = t[idx]
            if d[val] in value_set:
                return False
            value_set.add(d[val])
    return True



        
if __name__ == '__main__':
    s = 'egg'
    t = 'add'
    print(isIsomorphic(s,t))

    s = "foo"
    t = "bar"
    print(isIsomorphic(s,t))

    s = "paper"
    t = "title"
    print(isIsomorphic(s,t))

    s = "aba"
    t = "baa"
    print(isIsomorphic(s,t))