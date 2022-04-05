solution = lambda t, l=[]: max(l) if not t else solution(t[1:],
                                                         [max(x, y) + z for x, y, z in zip([0] + l, l + [0], t[0])])
"""
1. 한 층씩 제거하며, 그 층에서 계산한 최대 이동거리 배열을 계산하여, 한 층을 제거한 traingle을 첫번째 input, 이동거리 배열을 두 번째 input으로 넣어줍니다. 
2. 따라서 traingle이 없으면 제거할 층이 없으므로 최종 조건입니다. 3. [0] + l, l + [0] 을 이용하여 모서리 조건을 해결해줍니다.
"""
