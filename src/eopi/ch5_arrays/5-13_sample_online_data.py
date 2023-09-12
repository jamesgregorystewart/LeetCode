""" Sample Online Data 

Write a program that takes as input a size k, and a stream of input and returns
a subset of the input stream of size k where any permutation is equally likely
"""

"""
    Idea:
    - Fill the result array with first k elements from stream
    - On each subsequent input from the stream, choose whether it will belong based on some probability
    - If it will be included then choose the element to be removed from the sample set

Time: O(n)
Space: O(k)

Trick:
    - Recognizing the probability of a new packet being selected for the random sample with probability k/n

"""

from typing import List, Iterator
import itertools
from random import randint

def online_sample(stream: Iterator[int], k: int) -> List[int]:
    running_sample = list(itertools.islice(stream, k))

    num_seen_so_far = k
    for packet in stream:
        packet_to_replace = randint(0, num_seen_so_far)
        if packet_to_replace < k:
            running_sample[packet_to_replace] = packet
        num_seen_so_far += 1

    return running_sample

print(online_sample(['p','q','r','t','u','v'], 2))
