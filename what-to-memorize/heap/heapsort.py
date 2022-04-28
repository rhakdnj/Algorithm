import sys
import heapq


def input():
    return sys.stdin.readline().rstrip()


def heapsort(nums):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)

    sorted_nums = []
    while heap:
        sorted_nums.append(heapq.heappop(heap))
    return sorted_nums


print(heapsort([4, 1, 7, 3, 8, 5]))
