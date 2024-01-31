class Solution:
    def myAtoi(self, s: str) -> int:
        integer, sign = 0, 1
        i = 0
        while i < len(s) and s[i] == " ":
            i += 1
        if i < len(s) and s[i] == "+":
            i += 1
        elif i < len(s) and s[i] == "-":
            sign = -1
            i += 1
        digits = set(str(x) for x in range(10))
        while i < len(s) and s[i] in digits:
            integer = int(s[i]) + integer * 10
            i += 1
            if sign * integer >= (2**31 - 1):
                return 2**31 - 1
            if sign * integer <= -2**31:
                return -2**31
        return sign * integer

print(Solution().myAtoi("42"))