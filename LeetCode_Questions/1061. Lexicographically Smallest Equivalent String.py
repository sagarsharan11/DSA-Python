# Input: s1 = "parker", s2 = "morris", baseStr = "parser"
# Output: "makkek"
# Explanation: Based on the equivalency information in s1 and s2, we can group their characters as [m,p], [a,o], [k,r,s], [e,i].
# The characters in each group are equivalent and sorted in lexicographical order.
# So the answer is "makkek".

# Input: s1 = "hello", s2 = "world", baseStr = "hold"
# Output: "hdld"
# Explanation: Based on the equivalency information in s1 and s2, we can group their characters as [h,w], [d,e,o], [l,r].
# So only the second letter 'o' in baseStr is changed to 'd', the answer is "hdld".

# Input: s1 = "leetcode", s2 = "programs", baseStr = "sourcecode"
# Output: "aauaaaaada"
# Explanation: We group the equivalent characters in s1 and s2 as [a,o,e,r,s,c], [l,p], [g,t] and [d,m], thus all letters in baseStr except 'u' and 'd' are transformed to 'a', the answer is "aauaaaaada".


def smallestEquivalentString(s1, s2, baseStr):
    UF = {}
    def find(x):
        UF.setdefault(x,x)
        if x != UF[x]:
            UF[x] = find(UF[x])
        return UF[x]
    
    def union(x,y):
        rootX = find(x)
        rootY = find(y)
        if rootX>rootY:
            UF[rootX] = rootY
        else:
            UF[rootY] = rootX
    
    for i in range(len(s1)):
        union(s1[i],s2[i])
    
    res = []
    for c in baseStr:
        res.append(find(c))
        
    return ''.join(res)




if __name__ == "__main__":
    s1 = 'parker'
    s2 = 'morris'
    baseStr = 'parser'
    print(smallestEquivalentString(s1, s2, baseStr))

    s1 = "hello"
    s2 = "world"
    baseStr = "hold"
    print(smallestEquivalentString(s1, s2, baseStr))

    s1 = "leetcode"
    s2 = "programs"
    baseStr = "sourcecode"
    print(smallestEquivalentString(s1, s2, baseStr))