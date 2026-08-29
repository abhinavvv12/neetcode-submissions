class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1 = {}
        hash2 = {}

        for ch in s:
            hash1[ch] = hash1.get(ch,0)+1
        for ch in t:
            hash2[ch] = hash2.get(ch,0)+1

        return hash1 == hash2
