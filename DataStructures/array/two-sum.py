#https://leetcode.com/problems/two-sum/

class Solution:

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        d = {}
        #Itereate with both index & number
        for i, num in enumerate(nums):
            r = target - num 
            if r in d: return [d[r], i] #If remainder found in dict return [index & reminder[Value from dict]]
            d[num] = i #Store Number & Index as Key Value Pair


a = Solution()
print(a.twoSum([1,3,4,56,64],60))