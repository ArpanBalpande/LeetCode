class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = [None] * len(indices)
        for i in range(len(indices)):
            result[indices[i]] = s[i]
        return ''.join(result)