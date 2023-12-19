class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = 0
        numDict = {}
        for num in nums:
            if num not in numDict:
                nums[unique] = num
                numDict[num] = True
                unique += 1
        return unique