class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        postfix = 1
        retList = [0]*len(nums)
        # do the multiplication before nums[i]
        for i in range(len(nums)):
            retList[i] = prefix
            prefix *= nums[i]
        # do the multiplication after nums[i]
        for i in range((len(nums) - 1), -1, -1):
            retList[i] *= postfix
            postfix *= nums[i]
        return retList