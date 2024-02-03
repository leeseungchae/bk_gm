"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
"""


def longestCommonPrefix(self, strs: List[str]) -> str:
    strs.sort()
    s_len = len(strs[0])

    a = []

    for i in range(s_len):
        if strs[0][i] == strs[-1][i]:
            a.append(strs[0][i])
        else:
            break
    return ''.join(a)