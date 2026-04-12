class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        fp = 0
        rp = 0
        c = []
        for i in range(0,len(nums)):
            if(nums[i] == 1):
                fp += 1
                #print("fp, rp = ", fp, rp)
                c.append(fp - rp)
            else:
                fp += 1
                rp = fp
                #print("fp, rp = ", fp, rp)
        if (c):
            return max(c)
        else:
            return 0
