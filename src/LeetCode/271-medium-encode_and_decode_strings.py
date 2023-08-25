# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.
#
# Machine 1 (sender) has the function:
#
# string encode(vector<string> strs) {
#   // ... your code
#   return encoded_string;
# }
# Machine 2 (receiver) has the function:
# vector<string> decode(string s) {
#   //... your code
#   return strs;
# }
# So Machine 1 does:
#
# string encoded_string = encode(strs);
# and Machine 2 does:
#
# vector<string> strs2 = decode(encoded_string);
# strs2 in Machine 2 should be the same as strs in Machine 1.
#
# Implement the encode and decode methods.
#
# You are not allowed to solve the problem using any serialize methods (such as eval).
#
#  
#
# Example 1:
#
# Input: dummy_input = ["Hello","World"]
# Output: ["Hello","World"]
# Explanation:
# Machine 1:
# Codec encoder = new Codec();
# String msg = encoder.encode(strs);
# Machine 1 ---msg---> Machine 2
#
# Machine 2:
# Codec decoder = new Codec();
# String[] strs = decoder.decode(msg);
# Example 2:
#
# Input: dummy_input = [""]
# Output: [""]
#  
#
# Constraints:
#
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] contains any possible characters out of 256 valid ASCII characters.
#  
#
# Follow up: Could you write a generalized algorithm to work on any possible set of characters?


"""
Idea: choose a delimiter (/:) and append to result string the length of string, escape character, then the string
"""

from typing import List

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ""
        for s in strs:
            res+=str(len(s))+"/:"+s
        return res

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """

        res = []
        pointer = 0
        while pointer < len(s):
            esc_seek = 3
            while "/:" not in s[pointer:pointer+esc_seek]:
                esc_seek+=1
            str_len = int(s[pointer:pointer+esc_seek-2])
            str_segment = s[pointer+esc_seek:pointer+esc_seek+str_len]
            res.append(str_segment)
            pointer += esc_seek + str_len 
        return res


strs = ["Hello", "World"]
# Your Codec object will be instantiated and called as such:
codec = Codec()
print(codec.decode(codec.encode(strs)))
print(codec.decode(codec.encode(["", "4 "])))
