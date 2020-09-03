class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        Max = max(candies)
        return [ candy + extraCandies >= Max for candy in candies]