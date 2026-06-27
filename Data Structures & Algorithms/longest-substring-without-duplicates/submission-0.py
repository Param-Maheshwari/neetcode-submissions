class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range (len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1) # Window is inclusive on both ends — e.g. l=1, r=3 covers indices 1,2,3 → size = 3, not 2.
        return res

