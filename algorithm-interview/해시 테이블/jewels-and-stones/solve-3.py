import collections


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = collections.Counter(stones)
        count = 0

        # Counter outputs 0 instead of raising a KeyError in case of a non-existent key.
        for char in jewels:
            count += freqs[char]
