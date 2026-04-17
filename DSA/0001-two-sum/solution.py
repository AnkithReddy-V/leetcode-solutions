class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        have ={}

        for i, num in enumerate(nums):
            want = target - num

            if want in have:
                return [have[want], i]
        
            have[num] = i
                
