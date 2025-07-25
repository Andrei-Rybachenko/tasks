from collections import Counter


class Solution:
    def longest_palindrome(self, s: str) -> int:
        count = Counter(s)
        length = 0
        odd_found = False

        for i in count.values():
            length += (i // 2) * 2
            if i % 2 == 1:
                odd_found = True

        if odd_found:
            length += 1

        return length

