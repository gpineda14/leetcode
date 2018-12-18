import heapq
def findKthLargest(nums, k):
    heapq.heapify(nums)
    return heapq.nlargest(k, nums)[-1]
