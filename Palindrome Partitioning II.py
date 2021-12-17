'''
iven a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
Example 2:

Input: s = "a"
Output: 0
Example 3:

Input: s = "ab"
Output: 1
'''
class Solution:
    def minCut(self, s: str) -> int:
        return self.ans(s,0,len(s)-1)
    def ans(self,s,start,end):
        if self.ispall(s,start,end) is True:
            return 0
        
        ans=100000
        
        for currcut in range (start,end):
            left= self.ans(s,start,currcut)
            right= self.ans(s,currcut+1,end)
            tempans=1+left+right
            ans=min(ans,tempans)
        return ans
        
        
    def ispall(self,s,start,end):
        while(start<=end):
            if s[start]!=s[end]:
                return False

            start=start+1
            end=end-1
        return True
