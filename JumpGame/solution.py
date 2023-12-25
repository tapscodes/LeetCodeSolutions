class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # edge case, no jumps/positions at all
        if(len(nums) < 1):
            return True
        # set goal and starting positions
        curr = 0
        remainder = len(nums) - 1
        leaps = nums[curr]
        # if initial leap reaches the end (or array is empty/1 element)
        if(leaps >= remainder):
            return True
        # main logic
        while(leaps > 0):
            curr_leap = 0
            max_leap = 0
            # check for largest leap remaining
            for i in range(1, leaps + 1):
                if(max_leap < (i + nums[curr+i])):
                    max_leap = i+nums[curr+i]
                    curr_leap = i
            # leap/end if possible
            if(curr + max_leap >= remainder):
                return True
            curr += curr_leap
            # update leaps for next loop or ends loop by setting leaps to 0 (since we didn't move)
            if(max_leap > 0):
                leaps = nums[curr]
            else:
                leaps = 0
        # if there's not enough leaps left to reach goal
        return False