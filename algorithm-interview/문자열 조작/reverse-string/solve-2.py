from typing import *


class Solution:
    def reverseString(self, s: List[str]) -> None:
        # s.reverse()
        # s = s[::-1] 그냥 리스트 객체를 생성 해서 할당
        # s[:] 기존의 객체 리스트 값을  s[: : -1] 값으로 변경
        s[:] = s[::-1]


if __name__ == "__main__":
    solution = Solution()
    s = ["h", "e", "l", "l", "o"]
    solution.reverseString(s)
    print(s)
