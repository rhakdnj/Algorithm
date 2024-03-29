from typing import *


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for start in range(len(gas)):
            fuel = 0
            can_travel = True
            for i in range(start, len(gas) + start):
                index = i % len(gas)

                can_travel = True
                if gas[index] + fuel < cost[index]:
                    can_travel = False
                    break
                else:
                    fuel += gas[index] - cost[index]
            if can_travel:
                return start
        return -1


gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
sol = Solution()
print(sol.canCompleteCircuit(gas, cost))
