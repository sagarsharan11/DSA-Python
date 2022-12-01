# Input: s = "book"
# Output: true
# Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.

# Input: s = "textbook"
# Output: false
# Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
# Notice that the vowel o is counted twice.


def halvesAreAlike(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    if len(s)%2==0:
        mid_len = int(len(s)/2)
        a, b = s[:mid_len], s[mid_len:]
        val_a, val_b = [], []
        for i in range(mid_len):
            if a[i] in vowels:
                val_a.append(a[i])
            if b[i] in vowels:
                val_b.append(b[i])
        if len(val_a)==len(val_b):
            return True
        else:
            return False




if __name__ == "__main__":
    s = "book"
    print(halvesAreAlike(s))

    s = "textbook"
    print(halvesAreAlike(s))

    s = "AbCdEfGh"
    print(halvesAreAlike(s))



