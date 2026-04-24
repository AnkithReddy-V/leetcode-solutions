class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dupe = set()

        for n in nums:
            if n in dupe:
                return True
            dupe.add(n)
        return False
        