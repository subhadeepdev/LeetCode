class Solution:
    def longestPalindrome(self, s: str) -> str:
        t = '#'.join('@' + s + '$')
        center, lengths = 0, [0] * len(t)

        for i in range(1, len(t) - 1):
            right = center + lengths[center]
            mirror = center - (i - center)
            lengths[i] = right > i and min(right - i, lengths[mirror])

            while t[i + 1 + lengths[i]] == t[i - 1 - lengths[i]]:
                lengths[i] += 1

            if i + lengths[i] > right:
                center = i

        maxLength, bestCenter = max((length, i) for i, length in enumerate(lengths))
        return s[(bestCenter - maxLength) // 2: (bestCenter + maxLength) // 2]

print(Solution().longestPalindrome("babad"))