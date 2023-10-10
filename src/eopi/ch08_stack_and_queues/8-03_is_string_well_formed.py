"""Is a String Well-Formed?"""

"""
E.g. '{},[],(,)' is well-formed

"""

def is_well_formed(s: str) -> bool:
    openers = ['(', '{', '[']
    closers = [')', '}', ']']
    stack = []

    for c in s:
        if c in openers:
            stack.append(c)
        elif c in closers:
            if not stack or stack[-1] != openers[closers.index(c)]:
                return False
            stack.pop()

    return True

print(is_well_formed('{},[],()'))
print(is_well_formed('([]){()}'))
print(is_well_formed('{)'))
