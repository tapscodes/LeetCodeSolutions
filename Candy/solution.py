class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1]*len(ratings)
        update = []
        # loop from start to second to last variable and check element 1 right
        for i in range(0, len(ratings) - 1):
            # if left greater than right
            if(ratings[i] > ratings[i+1]):
               update.append(i)
            # if right greater than left
            elif(ratings[i] < ratings[i+1]):
                if(candies[i] >= candies[i+1]):
                    candies[i+1] = candies[i] + 1
        # retroactively calculate items where left was > right (goes from right->left in insert orer)
        for index in reversed(update):
            # check if candies even need an update
            if(candies[index] <= candies[index+1]):
                candies[index] = candies[index+1] + 1
        # generates sum of candies
        return sum(candies)