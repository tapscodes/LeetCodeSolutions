class Solution:
    def jump(self, nums: List[int]) -> int:
        # edge case, no jumps/positions at all
        if(len(nums) <= 1):
            return 0
        # set goal and starting positions
        curr = 0
        remainder = len(nums) - 1
        leaps = nums[curr]
        total_leaps = 0
        # if initial leap reaches the end
        if(leaps >= remainder):
            return 1
        # main logic
        while(leaps > 0):
            curr_leap = 0
            max_leap = 0
            total_leaps += 1
            # check for largest leap remaining
            for i in range(1, leaps + 1):
                if(max_leap < (i + nums[curr+i])):
                    max_leap = i+nums[curr+i]
                    curr_leap = i
            # leap/end if possible
            if(curr + max_leap >= remainder):
                return total_leaps + 1
            curr += curr_leap
            # update leaps for next loop or ends loop by setting leaps to 0 (since we didn't move)
            if(max_leap > curr_leap):
                leaps = nums[curr]
            else:
                leaps = 0
        # if there's not enough leaps left to reach goal
        return -1