class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if(len(nums) > 1):
            k %= len(nums)
            temp = [0] * k
            j = 0
            # stores the ending 'k' elements
            for i in range(len(nums) - k, len(nums), 1):
                temp[j] = nums[i]
                j += 1
            # moves the non-k elements, k values to the right
            for i in range(len(nums) - 1, k - 1, -1):
                nums[i] = nums[i-k]
            # puts the ending 'k' elements at their spot in the front
            for i in range(0, k, 1):
                nums[i] = temp[i]