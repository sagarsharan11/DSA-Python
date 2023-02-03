# Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
# Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
# Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
# "dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
# "ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".

# Input: words = ["cat","dog","catdog"]
# Output: ["catdog"]

# Input: words = ["a","b","ab","abc"]
# Output: ["ab"]

"""
APPROACH
1. store every-word in dict with word as key and its len as value | dict1
2. reverse order of len of words | loop for len less that that word update if that words is in selected word | dict2 update | will happen for every word
3. iterate over dict2 and output the words with count >= 2
"""

# {'hippopotamuses': 0,
#  'ratcatdogcat': 0,
#  'catsdogcats': 0,
#  'dogcatsdog': 0,
#  'cats': 0,
#  'cat': 0,
#  'dog': 0,
#  'rat': 0}


def findAllConcatenatedWordsInADict(words):
    sort_words = sorted(words, reverse=True, key=len)

    word_count = {x:0 for x in sort_words}
    idx = []
    for i in range(len(sort_words)):
        base_wrd = sort_words[i]
        # print("Got new Word:", base_wrd)
        for curr_wrd in sort_words[i+1:]:
            if curr_wrd in base_wrd:
                word_count[sort_words[i]] += 1
                base_wrd = base_wrd.replace(curr_wrd,'')
                # print("Change in Base Word Detected:", base_wrd)
                if len(base_wrd) == 0:
                    idx.append(sort_words[i])
    # print(idx)
    # print(word_count)
    return idx #[x for x in word_count if word_count[x]>=2]


def findAllConcatenatedWordsInADict(words):
    d = set(words)
            
    def dfs(word):
        for i in range(1, len(word)):
            prefix = word[:i]
            suffix = word[i:]
            
            if prefix in d and suffix in d:
                return True
            if prefix in d and dfs(suffix):
                return True
            if suffix in d and dfs(prefix):
                return True
        
        return False

    res = []
    for word in words:
        if dfs(word):
            res.append(word)

    return res







if __name__ == "__main__":
    words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
    print(findAllConcatenatedWordsInADict(words))

    words = ["cat","dog","catdog"]
    print(findAllConcatenatedWordsInADict(words))

    words = ["a","b","ab","abc"]
    print(findAllConcatenatedWordsInADict(words))


