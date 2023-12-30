class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # need enough gas to traverse
        if(sum(gas) < sum(cost)):
            return -1
        # start sim
        tank = 0
        index = 0

        # simulation
        for i in range(len(gas)):
            tank += gas[i]-cost[i]
            if(tank < 0):
                tank = 0
                index = i + 1
        return index