class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        op = []
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    op.append(i)
                    op.append(j)
                    return op
