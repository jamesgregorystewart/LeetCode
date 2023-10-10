""" Normalize Pathnames """

"""
Write a program which given a pathname returns its shortest path.

E.g. /src/../src/bin/./etc -> /src/bin/etc
"""

def normalize_pathname(s: str) -> str:
    stack = []

    for dir in s.split('/'):
        if dir == '..':
            if stack:
                stack.pop()
        elif dir and dir != '.':
            stack.append(dir)

    pathname = ""
    for dir in stack:
        pathname += dir + "/"
    return pathname

print(normalize_pathname("/src/../src/bin/./etc"))
