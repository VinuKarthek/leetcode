class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        #Set Removes Duplicates & Sorts the array 
        nums_set, i = set(nums), 1
        #Start from 1 and increment till we find the first positive value
        while i in nums_set:
            i += 1
        return i

a = Solution()
print(a.firstMissingPositive([1,2,0]))

print(a.firstMissingPositive([3,4,-1,1]))

print(a.firstMissingPositive([7,8,9,11,12,12]))
