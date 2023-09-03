import timeit


class Solution:
    @staticmethod
    def bubblesort(nums: list[int]) ->list[int]:
        # Swap the elements to arrange in order
        for iter_num in range(len(nums)-1,0,-1):
            for idx in range(iter_num):
                if nums[idx]>nums[idx+1]:
                    temp = nums[idx]
                    nums[idx] = nums[idx+1]
                    nums[idx+1] = temp
        return nums
    
    @staticmethod
    def insertion_sort(InputList: list[int]) ->list[int]:
        for i in range(1, len(InputList)):
            j = i-1
            nxt_element = InputList[i]
        # Compare the current element with next one
        while (InputList[j] > nxt_element) and (j >= 0):
            InputList[j+1] = InputList[j]
            j=j-1
        InputList[j+1] = nxt_element
        return InputList

    @staticmethod
    def selection_sort(input_list):
        for idx in range(len(input_list)):
            min_idx = idx
            for j in range( idx +1, len(input_list)):
                if input_list[min_idx] > input_list[j]:
                    min_idx = j
            # Swap the minimum value with the compared value
            input_list[idx], input_list[min_idx] = input_list[min_idx], input_list[idx]
        return input_list


a = Solution()
list1 = [19,2,31,45,30,11,121,27]
print(a.bubblesort(list1))
print(a.insertion_sort(list1))
print(a.selection_sort(list1))


# Define the setup code (if any) required for the statement
setup_code = '''
from __main__ import Solution
import random
unsorted_list = [random.randint(1, 1000) for _ in range(800)]
list1 = unsorted_list
a = Solution()
'''

# Define the statement to time
stmt = 'a.bubblesort(list1)'

# Time the statement and print the result
time_taken = timeit.timeit(stmt='a.bubblesort(unsorted_list)', setup=setup_code, number=10)
print(f"Time taken bubblesort: {time_taken} seconds")
time_taken = timeit.timeit(stmt='a.insertion_sort(unsorted_list)', setup=setup_code, number=10)
print(f"Time taken insertion_sort: {time_taken} seconds")
time_taken = timeit.timeit(stmt='a.selection_sort(unsorted_list)', setup=setup_code, number=10)
print(f"Time taken selection_sort: {time_taken} seconds")