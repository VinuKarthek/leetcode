
class Solution:
    def binarySearch(self, arr:list[int], x:int) -> int:
        left = 0
        right = len(arr) - 1
        mid = 0
    
        while left <= right:
    
            mid = (right + left) // 2
    
            # If x is greater, ignore left half
            if arr[mid] < x:
                left = mid + 1
    
            # If x is smaller, ignore right half
            elif arr[mid] > x:
                right = mid - 1
    
            # means x is present at mid
            else:
                return mid
    
        # If we reach here, then the element was not present
        return -1

    def binarySearch1(self, search_list:list[int], find:int) -> int:
        l , r = 0, len(search_list)-1
        cur = 0
        for i in range(len(search_list)):
            print(l,r)

            cur = (l+r)//2
            
            item = search_list[cur]
            
            if find > item:
                l = cur
            elif find < item:
                r = cur
            else:
                return cur

        return None


search  = [0, 6, 10, 11, 20, 26, 38, 46, 48, 53, 66, 68, 77, 78, 80, 99, 100]
find = 46

solution = Solution()
print(solution.binarySearch(search, find))
print(solution.binarySearch1(search, find))