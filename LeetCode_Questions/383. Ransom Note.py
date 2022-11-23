# Input: ransomNote = "a", magazine = "b"
# Output: false

# Input: ransomNote = "aa", magazine = "ab"
# Output: false

# Input: ransomNote = "aa", magazine = "aab"
# Output: true

# Input: ransomNote ="fffbfg", magazine ="effjfggbffjdgbjjhhdegh"


# def canConstruct(ransomNote, magazine):
#     if (ransomNote == magazine)|(ransomNote[::-1] == magazine):
#         return True
#     elif ransomNote in magazine:
#         return True
#     else:
#         return False


### brute force approach
def canConstruct(ransomNote, magazine):
    dict_ransomNote = dict()
    for i in ransomNote:
        if i in dict_ransomNote:
            dict_ransomNote[i]+=1
        else:
            dict_ransomNote[i] = 1
    dict_magazine = dict()
    for i in magazine:
        if i in dict_magazine:
            dict_magazine[i]+=1
        else:
            dict_magazine[i] = 1
    checker = []
    for i in ransomNote:
        if i in magazine:
            if dict_ransomNote[i] <= dict_magazine[i]:
                checker.append('True')
            else:
                checker.append('False')
        else:
            checker.append('False')
    if 'False' in checker:
        return False
    else:
        return True

    
## Optimal Approach
# def canConstruct(ransomNote, magazine):
#     for c in ransomNote:
#             if c not in magazine:
#                 return False
#             magazine = magazine.replace(c, '', 1)
#     return True
       


    
if __name__ == "__main__":
    # ransomNote = "a"
    # magazine = "b"
    # print(canConstruct(ransomNote, magazine))

    # ransomNote = "aa"
    # magazine = "ab"
    # print(canConstruct(ransomNote, magazine))

    # ransomNote = "aa"
    # magazine = "aab"
    # print(canConstruct(ransomNote, magazine))

    ransomNote = "fihjjjjei"
    magazine = "hjibagacbhadfaefdjaeaebgi"
    print(canConstruct(ransomNote, magazine))