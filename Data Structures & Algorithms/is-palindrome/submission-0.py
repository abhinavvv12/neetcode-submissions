class Solution:
    def isPalindrome(self, s: str) -> bool:
        low = 0
        high = len(s) - 1

        while low < high:

            # Skip non-alphanumeric characters from left
            while low < high and not s[low].isalnum():
                low += 1

            # Skip non-alphanumeric characters from right
            while low < high and not s[high].isalnum():
                high -= 1

            # Compare characters
            if s[low].lower() != s[high].lower():
                return False

            low += 1
            high -= 1

        return True