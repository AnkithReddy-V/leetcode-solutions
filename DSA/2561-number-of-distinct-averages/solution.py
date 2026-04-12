class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        j = (len(nums) - 1)
        avg = set()
        for k in range(0, (len(nums)//2+1)):
            avg.add(nums[i] + nums[j])
            i += 1
            j -= 1
        return len(avg)

