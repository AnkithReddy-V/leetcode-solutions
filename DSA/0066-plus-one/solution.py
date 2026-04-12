class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        unit = len(digits) - 1
        for i in range(len(digits)):
            if(digits[unit] == 9):
                digits[unit] = 0
                unit -= 1
            else:
                digits[unit] += 1
                break
        if(digits[0] == 0):
            digits.insert(0, 1)
        return(digits)
