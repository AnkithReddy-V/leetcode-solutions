class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s, freq_t = {}, {}
        freq_s = Counter(s)
        freq_t = Counter(t)
        if (freq_t == freq_s):
            return True
        else:
            return False
