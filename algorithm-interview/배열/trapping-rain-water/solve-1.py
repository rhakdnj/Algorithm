"""
최대 높이는 3이지만 100이어도 관계는 없다. 막대는 높고 낮음에 무관하게, 전체 부피에 영향을 끼치지 않으면서
그저 왼쪽과 오른쪽을 가르는 장벽 역할을 한다.
volume += left_max - height[left]
volume += right_max -height[right]
"""
from typing import *


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max, right_max = max(height[left], left_max), \
                                  max(height[right], right_max)
            # 더 높은 쪽을 향해 투 포인터 이동
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1
        return volume


if __name__ == "__main__":
    solution = Solution()
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    res = solution.trap(height)
    print(res)

