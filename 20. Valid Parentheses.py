class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {')': '(', '}': '{', ']': '['}
        for char in s:
            if len(stack) != 0 and char in pair and pair[char] == stack[-1]:
                stack.pop()
                continue
            stack.append(char)
        return len(stack) == 0
        