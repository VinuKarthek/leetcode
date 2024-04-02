
class Solution:
    def binarySearch(self, search_list:list[int], find:int) -> int:
        l , r = 0, len(search_list)
        cur = 0
        for i in range(len(search_list)):
            if cur == (l+r+1)//2: return None
            cur = (l+r+1)//2
            item = search_list[cur]
            print(l,r)

            if item == find: return cur
            if find > item:
                l = cur
            else:
                r = cur
        
        return None


search  = [0, 6, 10, 11, 20, 26, 38, 46, 48, 53, 66, 68, 77, 78, 80, 99, 100]
find = 12

solution = Solution()
print(solution.binarySearch(search, find))