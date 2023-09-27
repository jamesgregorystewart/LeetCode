""" 981 MEDIUM Time Based Key-Value Store """

# Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.
#
# Implement the TimeMap class:
#
# TimeMap() Initializes the object of the data structure.
# void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
# String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
#  
#
# Example 1:
#
# Input
# ["TimeMap", "set", "get", "get", "set", "get", "get"]
# [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
# Output
# [null, null, "bar", "bar", null, "bar2", "bar2"]
#
# Explanation
# TimeMap timeMap = new TimeMap();
# timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
# timeMap.get("foo", 1);         // return "bar"
# timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
# timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
# timeMap.get("foo", 4);         // return "bar2"
# timeMap.get("foo", 5);         // return "bar2"
#  
#
# Constraints:
#
# 1 <= key.length, value.length <= 100
# key and value consist of lowercase English letters and digits.
# 1 <= timestamp <= 107
# All the timestamps timestamp of set are strictly increasing.
# At most 2 * 105 calls will be made to set and get.

"""
Time: O(log(n))
Space: O(n)
"""

from typing import Dict, List, Tuple

class TimeMap:

    def __init__(self):
        self.time_map: Dict[str, List(Tuple(str, int))] = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.time_map.keys():
            self.time_map[key].append((value, timestamp))
        else:
            self.time_map[key] = [(value, timestamp)]
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
        values = self.time_map[key] 
        if len(values) > 0 and values[0][1] > timestamp:
            return ""
        
        # Binary search for the highest timestamp less than timestamp
        l, r = 0, len(values)-1
        while l <= r:
            mid = l + (r - l) // 2
            if values[mid][1] <= timestamp and (mid == len(values)-1 or values[mid+1][1] > timestamp):
                return values[mid][0]
            if values[mid][1] < timestamp:
                l = mid + 1
            else:
                r = mid - 1
        return values[l][0]

# Your TimeMap object will be instantiated and called as such:
obj = TimeMap()
obj.set('2','t0',0)
print(obj.get('2',1))
obj.set('2', 't2', 2)
print(obj.time_map)
print(obj.get('2', 3))
print(obj.get('3', 4))
obj.set('2', 't4', 4)
obj.set('2', 't6', 6)
obj.set('2', 't7', 7)
obj.set('2', 't9', 9)
print(obj.get('2', 5))
print(obj.get('2', 8))
print(obj.get('2', 9))
print(obj.get('2', 10))
print(obj.get('2', -1))
