class Solution:
    def calculate(self, s: str) -> int:
        num, sign, answer = 0, 1, 0
        stack = [1]

        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == "(":
                stack.append(sign)
            elif char == ")":
                stack.pop()
            elif char == "+" or char == "-":
                answer += sign * num
                sign = (1 if char == "+" else -1) * stack[-1]
                num = 0
        return answer + sign * num

                
print(Solution().calculate("(1+(4+5+2)-3)+(6+8)"))