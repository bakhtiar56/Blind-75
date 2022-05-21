class Solution:
  '''
  Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Input: nums = [3,2,4], target = 6
Output: [1,2]
  
  '''
  
  
  
  
  
  
  
  
  
  
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #compute differencve between each value and target
        #if difference in hashmap, return the value index and difference index
        #else store the value index pair in hashmap
        store hashmap for every value
        
        a=nums
        
        hash_map={}
        result=[]
        
#         def find_largest_num_less_than_z(arr,z):
#             max=1000000000000000000000
#             for idx,x in enumerate(arr):
#                 if x<z and x<max:
#                     max=x
#                 elif x>z and idx>0:
#                     return idx-1
#             return len(arr)-1
            
        
        # largest_index=find_largest_num_less_than_z(a,target)
        # print(largest_index)
        
        
        
        
#         def binary_search(x,t):
#             #based on target t and sorted array x, return in which area of array, to find the two numbers
            
           
#             l=len(x)
#             mid=l//2
#             left=x[0:mid+1]
#             right=x[mid+1:]
#             if t<x[mid]:
#                 return left,0
#             else:
#                 return right,mid
#         arr,offset=binary_search(a,target)
        # print(arr)
        arr=a
        # print(arr)
        for idx,x in enumerate(arr):
            try:
                
                inter=target-x
                y=hash_map[inter]
                result.extend([idx,y])
            except KeyError:
                hash_map[x]=idx
            
        return result
