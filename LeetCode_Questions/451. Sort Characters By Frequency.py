# Input: s = "tree"
# Output: "eert"
# Explanation: 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.


# Input: s = "cccaaa"
# Output: "aaaccc"
# Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
# Note that "cacaca" is incorrect, as the same characters must be together.


# Input: s = "Aabb"
# Output: "bbAa"
# Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.

def frequencySort(s):
    s_dict = {}
    for i in range(len(s)):
        if s[i] not in s_dict:
            s_dict.update({s[i]:1})
        elif s[i] in s_dict:
            counter = s_dict[s[i]] + 1
            s_dict.update({s[i]:counter})
    s_list = sorted(s_dict.items(), key=lambda x:x[1])[::-1]
    s_word = ''
    for word in s_list:
        s_word+=word[0]*s_dict[word[0]]
    return s_word

if __name__=="__main__":
    s='tree'
    print(frequencySort(s))

    s='cccaaa'
    print(frequencySort(s))

    s='Aabb'
    print(frequencySort(s))





