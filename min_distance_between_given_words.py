words_list = ['the', 'quick', 'brown', 'fox', 'quick']
words_list2 = ['axa', 'ffn', 'ty', 'bs', 'oin', 'bs', 'axa']


def min_distance_between_words(s, word1, word2):
    distance = -1
    if not word1 in s or not word2 in s:
        return False
    flag = False
    for word in s:
        if flag or word == word1:
            flag = True
            distance += 1
        if word == word2 and not flag:
            return 1
        if word == word2:
            break
    return distance


print(min_distance_between_words(s=words_list2, word1="bs", word2="axa"))
