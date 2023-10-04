class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def contained(string1: str, string2: str) -> bool:
            sort_string1 = sorted(list(string1))
            sort_string2 = sorted(list(string2))
            i, j = 0, 0
            while i < len(string1):
                if j >= len(sort_string2):
                    return False
                if sort_string1[i] == sort_string2[j]:
                    i += 1
                j +=1
            return True

        if not contained(t, s):
            return ""
        ans = s
        for i in range(len(s)):
            for j in range(i, len(s)):
                if contained(t, s[i: j + 1]) and len(ans) > (j - i + 1):
                    ans = s[i: j + 1]
        return ans

solution = Solution()
print(solution.minWindow("ADOBECODEBANC", "ABC"))