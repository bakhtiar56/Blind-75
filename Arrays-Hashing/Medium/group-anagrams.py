'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

'''




class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dic=defaultdict(list)
        
        
        for word in strs:
            counts=[0]*26 #for keeping counts of each letter a..z
                    
            for letter in word:
              #keep track of each letter occurance list with its set of acceptable anagrams
              #e.g. {("a":1,"n":2):["naa","ann"]...}
                    
                counts[ord(letter)-ord("a")]+=1
                  
            dic[tuple(counts)].append(word)
        return dic.values()
        
        
            
        
        
            
            
            
            
                
                
                    
                        
        
