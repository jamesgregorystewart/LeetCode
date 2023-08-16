# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
#
#  
#
# Example 1:
#
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:
#
# Input: strs = [""]
# Output: [[""]]
# Example 3:
#
# Input: strs = ["a"]
# Output: [["a"]]
#  
#
# Constraints:
#
# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.

'''
Idea: iterate through list, sorting each word and putting it into a map, key is the sorted word, value is list of words that sort to that same thing
O(n(m(log(m)))) / O(n*m)

'''

from typing import List, Dict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams: Dict[tuple, List[str]] = {}
        for s in strs:
            sorted_tuple = tuple(sorted(s))
            if sorted_tuple not in anagrams:
                anagrams[sorted_tuple] = [s]
            else:
                anagrams[sorted_tuple].append(s)
        # convert anagrams map into a list to return
        return list(anagrams.values())


solution = Solution()
print(solution.groupAnagrams(strs=["eat","tea","tan","ate","nat","bat"]))
print(solution.groupAnagrams(strs=[[""]]))
print(solution.groupAnagrams(strs=[["a"]]))
