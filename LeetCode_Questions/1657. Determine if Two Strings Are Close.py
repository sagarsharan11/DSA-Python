# Input: word1 = "abc", word2 = "bca"
# Output: true
# Explanation: You can attain word2 from word1 in 2 operations.
# Apply Operation 1: "abc" -> "acb"
# Apply Operation 1: "acb" -> "bca"


# Input: word1 = "a", word2 = "aa"
# Output: false
# Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.

# Input: word1 = "cabbba", word2 = "abbccc"
# Output: true
# Explanation: You can attain word2 from word1 in 3 operations.
# Apply Operation 1: "cabbba" -> "caabbb"
# Apply Operation 2: "caabbb" -> "baaccc"
# Apply Operation 2: "baaccc" -> "abbccc"

def closeStrings(word1, word2):
    if len(word1)!=len(word2):
        return False
    else:
        word1_dict, word2_dict = {}, {}
        for i in range(len(word1)):
            if word1[i] in word1_dict:
                count1 = word1_dict[word1[i]] + 1
                word1_dict.update({word1[i]: count1})
            elif word1[i]  not in word1_dict:
                word1_dict.update({word1[i]: 1})
            if word2[i] in word2_dict:
                count2 = word2_dict[word2[i]] + 1
                word2_dict.update({word2[i]: count2})
            elif word2[i] not in word2_dict:
                word2_dict.update({word2[i]: 1})
        if (set(word1_dict.keys()) == set(word2_dict.keys())) & (sorted(list(word1_dict.values())) == sorted(list(word2_dict.values()))):
            return True
        else:
            return False
   


if __name__=="__main__":
    word1 ="abbzzca"
    word2 ="babzzcz"
    print(closeStrings(word1, word2))

    word1 ="abc"
    word2 ="bca"
    print(closeStrings(word1, word2))

    word1 ="a"
    word2 ="aa"
    print(closeStrings(word1, word2))

    word1 ="cabbba"
    word2 ="abbccc"
    print(closeStrings(word1, word2))

    word1 = "aaabbbbccddeeeeefffff"
    word2 = "aaaaabbcccdddeeeeffff"
    print(closeStrings(word1, word2))