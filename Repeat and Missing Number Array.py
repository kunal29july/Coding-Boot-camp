'''
Example:

Input:[3 1 2 5 3] 

Output:[3, 4] 

A = 3, B = 4
'''
class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        res=[]
        d={}
        for i in A:
            if i not in d:
                d[i]=1
            else:
                d[i]=d[i]+1
        for i in A:
            if d[i]==2:
                res.append(i)
                break
        p=1
        for i in set(A):
            if p==i:
                p=p+1
        res.append(p)
        return(res)
            
