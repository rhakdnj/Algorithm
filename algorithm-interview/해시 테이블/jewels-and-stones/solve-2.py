import collections


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = collections.defaultdict(int)
        count = 0

        for char in stones:
            freqs[char] += 1

        # if char not in freqs, freqs[char] = 0 (defaultdict(int))
        for char in jewels:
            count += freqs[char]

        return count