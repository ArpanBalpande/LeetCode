class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum(stone in J for stone in S)