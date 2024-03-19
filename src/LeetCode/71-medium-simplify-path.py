from typing import List


class Solution:
    def simplifyPath(self, path: str) -> str:
        path_parts = path.split("/")
        ans: List[str] = []
        for part in path_parts:
            if part == "..":
                if ans:
                    ans.pop()
            elif part == "/" or part == "." or part == "":
                continue
            else:
                ans.append("/" + part)

        if not ans:
            ans.append("/")
        return "".join(ans)


solution = Solution()
print(solution.simplifyPath("/home/"))
print(solution.simplifyPath("/../"))
print(solution.simplifyPath("/home//foo/"))
print(solution.simplifyPath("/home//foo/../."))
