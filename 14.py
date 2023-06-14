# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".


# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.


class Solution:
    def longestCommonPrefix(self, strs):
        flag, k = 0,0
        common = ''
        x = strs[0]

        for i in x:
            for j in strs:
                if k<len(j) and j[k]==i:
                    flag = 1
                else:
                    flag = 0
                    break
            if flag == 1:
                common+=i
                k+=1
            else:
                return common
        return common

