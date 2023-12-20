class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = 2
        for i in range(unique, len(nums), 1):
            if(nums[i] != nums[unique-1] or nums[i] != nums[unique-2]):
                nums[unique] = nums[i]
                unique += 1
        return unique