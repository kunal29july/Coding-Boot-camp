'''
given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
Example 3:

Input: nums = [1,1]
Output: 1
Example 4:

Input: nums = [1,1,2]
Output: 1
'''
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #nums.sort()
        #print(nums)
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                
                d[i]=d[i]+1
                
            if d[i]>1:
                return i
