""" Compute Buildings with a View """

"""
Buildings are in order of east to west; return indices of buildings with a western view
"""

from typing import Iterator, List
from collections import namedtuple

def buildings_with_a_view(buildings: Iterator[int]) -> List[int]:
    Building = namedtuple('Building', ['position', 'height'])

    # create record of all the buildings in sequence
    prev_max, buildings_with_view, stack = float('-inf'), [], []
    for i, height in enumerate(buildings):
        stack.append(Building(i, height))
    
    # set prev_max to most west-facing building
    prev_max = stack[-1].height
    buildings_with_view.append(stack.pop().position)

    while stack:
        if stack[-1].height > prev_max:
            prev_max = stack[-1].height
            buildings_with_view.append(stack.pop().position)
        else:
            stack.pop()

    return buildings_with_view

print(buildings_with_a_view(iter([1,2,3,4])))
print(buildings_with_a_view(iter([4,3,2,1])))
