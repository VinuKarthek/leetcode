from collections import defaultdict

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        negative = defaultdict(int)
        positive = defaultdict(int)
        zeros = 0
        #Remove Duplicates & Group Positive/Negative/Zeros
        for num in nums:
            if num < 0:
                negative[num] += 1
            elif num > 0:
                positive[num] += 1
            else:
                zeros += 1
        
        result = []
        
        if zeros:
            #Search for (-n,0,n)
            for n in negative:
                if -n in positive:
                    result.append((0, n, -n))       
            if zeros > 2:
                result.append((0,0,0))

        for set1, set2 in ((negative, positive), (positive, negative)):
            set1Items = list(set1.items())
            print(set1)
            print(set2)
            print(set1Items)
            for i, (j, k) in enumerate(set1Items):
                for j2, k2 in set1Items[i:]:
                    if j != j2 or (j == j2 and k > 1):
                        if -j-j2 in set2:
                            result.append((j, j2, -j-j2))
        return result


a = Solution()
print(a.threeSum([-1,0,1,3,4,56,64,0,0]))