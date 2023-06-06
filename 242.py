# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false


# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.


def isAnagram(s,t):
    result = []

    if len(s) != len(t):
        return False

    for i in t:
        result.append(i)

    for i in s:
        if i in result:
            result.remove(i)
            continue
        else:
            return False

    return True

s = 'anagram'
t = 'nagaram'
#
#
#
#
#
# [OR]
#
#
#
#
#

def is_Anagram(s,t):
    return sorted(s) == sorted(t)

print(isAnagram(s,t))

