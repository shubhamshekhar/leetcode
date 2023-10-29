'''
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

 

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessairly unique.

'''


class Solution:

    def merge(self, nums, start, mid, end):
        i = start
        j = mid+1
        ptr = 0
        temp = []
        while i<=mid and j <=end:
            if nums[i] < nums[j]:
                temp.append(nums[i])
                i +=1
            else:
                temp.append(nums[j])
                j +=1
        while i<=mid:
            temp.append(nums[i])
            i +=1
        while j<=end:
            temp.append(nums[j])
            j +=1
        ptr = 0
        for i in range(start, end+1):
            nums[i] = temp[ptr]
            ptr += 1
        return nums


    def divide(self, nums, start, end):
        if start >= end:
            return
        mid = start + (end-start)//2
        self.divide(nums, start, mid)
        self.divide(nums, mid+1, end)

        return self.merge(nums, start, mid, end)

    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        return self.divide(nums, 0, len(nums)-1)

        
