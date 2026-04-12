class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for i in range(0, len(nums)):
            if(nums[i] in count):
                count[nums[i]] += 1
                #print(count)
            else:
                count.update({nums[i]: 1})
        return (max(count, key=count.get))

            
