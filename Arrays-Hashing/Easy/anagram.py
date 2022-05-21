class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count={}#count each letter in s
        t_count={}#count each letter in t
        f=0
        
        
        def bin_search(a):
            #do binary search to keep counts
            #to reduce runtime
            counts={}
            l=len(a)
            mid=l//2
            left=a[0:mid]
            right=a[mid:]
            for x in left:
                try:
                    counts[x]+=1
                except KeyError:
                    counts[x]=1
            for x in right:
                try:
                    counts[x]+=1
                except KeyError:
                    counts[x]=1
            return counts
        s_count=bin_search(s)
        t_count=bin_search(t)
        for x,y in t_count.items():
          #if count of each letter in s equal to that letter's count in t
          #increment f
          #if f=number of letters in s, return True
          #if any letter in t does not exist in s, return False
            try:
                if y==s_count[x]:
                    f+=1
            except KeyError:
                return False
        if f==len(s_count):
            return True
            
        
                
            
          
                
        
        
