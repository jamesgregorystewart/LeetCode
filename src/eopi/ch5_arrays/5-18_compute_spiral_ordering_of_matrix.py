""" Compute Spiral Ordering of 2D Array

Given an nxn matrix, return it's spiral ordering as an array
"""

""" Idea:
    - use a vector to modify the current position in one of four possible directions
    - loop for starting index, loop for direction to travel, loop to travel

Time: O(n^2)
Space: O(n^2) For resultant array
    
"""

from typing import List

def compute_spiral_order_of_matrix(matrix: List[List[int]]) -> List[int]:
    if len(matrix[0]) == 0:
        return []
    
    res = []
    movements = [[0,1],[1,0],[0,-1],[-1,0]]
    n, iteration = len(matrix[0]), 0

    for i in range(iteration, n - iteration, 1):
        if i > 0 and i < (n-iteration // 2):
            # we wrote the first element twice so we need to del last element added
            del res[len(res)-1]
        position = [i, i]
        for direction in range(4):
            if direction > 0:
                # we overstepped, so go back one step with previous vector
                # then take a step forward in new direction to prevent reprocessing
                position = [x - y for x, y in zip(position, movements[direction-1])]
                position = [x + y for x, y in zip(position, movements[direction])]
            vector = movements[direction]
            while position[0] >= i and position[0] < n - i and position[1] >= i and position[1] < n - i:
                    res.append(matrix[position[0]][position[1]])
                    position = [x + y for x, y in zip(position, vector)]
        iteration += 1

    return res

print(compute_spiral_order_of_matrix([[0,1],[3,2]]))
print(compute_spiral_order_of_matrix([[0,1,2],[7,8,3],[6,5,4]]))
print(compute_spiral_order_of_matrix([[0,1,2,3],[11,12,13,4],[10,15,14,5],[9,8,7,6]]))
