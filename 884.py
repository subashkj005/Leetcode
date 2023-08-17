# 884. Uncommon Words from Two Sentences
#
# A sentence is a string of single-space separated words where each word consists only of lowercase letters.
#
# A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
#
# Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.
#
#
#
# Example 1:
#
# Input: s1 = "this apple is sweet", s2 = "this apple is sour"
# Output: ["sweet","sour"]
# Example 2:
#
# Input: s1 = "apple apple", s2 = "banana"
# Output: ["banana"]
#
#
# Constraints:
#
# 1 <= s1.length, s2.length <= 200
# s1 and s2 consist of lowercase English letters and spaces.
# s1 and s2 do not have leading or trailing spaces.
# All the words in s1 and s2 are separated by a single space.

# Bruteforce
class Solution1:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s=s1+" "+s2
        word=""
        total_words=[]
        result=[]
        for i in range(len(s)+1):
            if i==len(s):
                total_words.append(word)
            elif s[i]!=" ":
                word+=s[i]
            else:
                total_words.append(word)
                word=""
        word_count = collections.Counter(total_words)
        result = [k for k,v in word_count.items() if v==1]
        return result


# Shorter
class Solution2:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s=s1.split()+s2.split()
        word_count = collections.Counter(s)
        return [ k for k,v in word_count.items() if v==1]