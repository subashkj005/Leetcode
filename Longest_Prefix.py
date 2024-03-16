words = ['geeksforgeeks', 'geeks', 'geek', 'geezer']


def find_the_longest_prefix(words):
    if len(words) == 0:
        return ""

    smallest_word = min(words)
    i = 0

    for char in smallest_word:
        for word in words:
            if i >= len(word) or word[i] != char:
                return smallest_word[:i]
        i += 1


print(find_the_longest_prefix(words))
