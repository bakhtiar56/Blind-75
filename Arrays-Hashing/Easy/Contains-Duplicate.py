'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 Input: nums = [1,2,3,1]
Output: true

Input: nums = [1,2,3,4]
Output: false
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
      
      #keep count of each letter
      #if at any point, count of one letter exceeds 1, return True
      #else at the end, return False
        counts={}
        for x in nums:
            try:
                counts[x]+=1
                if counts[x]>1:
                    return True
            except KeyError:
                counts[x]=1
        
        return False
        
