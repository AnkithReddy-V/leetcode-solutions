class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = [ch.lower() for ch in s if ch.isalnum()]
        l, r = 0, len(filtered) - 1
        
        while l < r:
            if filtered[l] != filtered[r]:
                return False

            l += 1
            r -= 1
        return True