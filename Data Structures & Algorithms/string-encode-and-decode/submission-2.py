class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            # Find '#'
            while s[j] != "#":
                j += 1

            # Get length
            length = int(s[i:j])

            # Move past '#'
            j += 1

            # Get the actual string
            res.append(s[j:j + length])

            # Move to the next encoded string
            i = j + length

        return res