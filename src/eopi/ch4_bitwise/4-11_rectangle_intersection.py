""" PROBLEM: Rectangle Intersection

Write a program which given two rectangles, returns the rectangle of their intersection, else None

"""

""" IDEA

"""

from collections import namedtuple

Rect = namedtuple('Rect', ('x', 'y', 'width', 'height'))
Rect.__doc__ += "A rectangle with a nearest point to origin, and dimensions."

r1 = Rect(4, 1, 2, 2)
r2 = Rect(3, 2, 2, 1)

def rectangle_intersection(r1: Rect, r2: Rect) -> Rect | None:
    def is_intersect(r1: Rect, r2: Rect) -> bool:
        return ((r1.x <= (r2.x + r2.width) and r2.x <= (r1.x + r1.width))
                and r1.y <= (r2.y + r2.height) and r2.y <= (r1.y + r1.height))

    if not is_intersect(r1, r2):
        return None
    return Rect(
                x = max(r1.x, r2.x),
                y = max(r1.y, r2.y),
                width = min(r1.x+r1.width, r2.x+r2.width) - max(r1.x, r2.x),
                height = min(r1.y+r1.height, r2.y+r2.height) - max(r1.y, r2.y),
            )

print(rectangle_intersection(r1, r2))
