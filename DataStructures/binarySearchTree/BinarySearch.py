
class Solution:
    def binarySearch(self, search_list:list[int], find:int) -> int:
        l = 0
        r = len(search_list)
        p=0
        for i in range(len(search_list)):
            if p == (l+r+1)//2: return None
            p = (l+r+1)//2
            item = search_list[p]
            print(l,r)

            if item == find: return p
            if find > item:
                l = p
            else:
                r = p
        
        return None


search  = [0, 6, 10, 11, 20, 26, 38, 46, 48, 53, 66, 68, 77, 78, 80, 99, 100]
find = 12

solution = Solution()
print(solution.binarySearch(search, find))