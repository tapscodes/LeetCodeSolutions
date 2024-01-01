class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        for i in range(1, len(height)):
            # check to the left for any water that will spawn
            lowest = 0
            j = i
            # if height is 0, no water is formed
            if(height[i] != 0):
                # loops all the way to left unless it breaks
                while(j > 0 and lowest < height[i]):
                    j -= 1
                    # if left wall is higher than any left wall previous
                    if(height[j] > lowest):
                        if(height[j] >= height[i]): #break if left wall is higher or == than right (max water filled)
                            water += (i - j - 1) * (height[i] - lowest) #calculate water to be added
                        else:
                            water += (i - j - 1) * (height[j] - lowest) #calculate water to be added      
                        lowest = height[j]
        return water