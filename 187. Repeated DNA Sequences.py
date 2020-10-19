class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dictionary = dict()
        for x in range(len(s)-9):
            dictionary[s[x:x+10]] = dictionary.get(s[x:x+10], 0) + 1
        return [k for k,v in dictionary.items() if v > 1]