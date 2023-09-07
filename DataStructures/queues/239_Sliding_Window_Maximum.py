from collections import deque

class Solution:

    # def maxSlidingWindow_typical(self, nums: List[int], k: int) -> List[int]:
        # n= len(nums)
        # out_list = []
        # w = nums[:k] #window
        # out_list.append(max(w))
        # for i in range(n-k+1):
        #     w.pop(0)
        #     w.append(nums[i+k-1])
        #     out_list.append(max(w))
        # return out_list

    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:

        dq = deque()
        res = []

        for i in range(k):
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)
        res.append(nums[dq[0]])

        for i in range(k,len(nums)):
            if dq and dq[0] == i - k:
                dq.popleft()
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            res.append(nums[dq[0]])

        return res