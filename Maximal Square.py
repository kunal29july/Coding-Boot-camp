
'''
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

 

Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4
Example 2:


Input: matrix = [["0","1"],["1","0"]]
Output: 1
Example 3:

Input: matrix = [["0"]]
Output: 0
'''
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        area=0
        row=len(matrix)
        col=len(matrix[0])
        for i in range (row):
            for j in range(col):
                if matrix[i][j]=="1":
        
                    tempans=self.ans(i,j,matrix,row,col)
                    area=max(area,tempans*tempans)
        return area
                
    def ans (self,currrow,currcol,matrix,row,col):
        if currrow<0 or currrow>=row or currcol<0 or currcol>=col or matrix[currrow][currcol]=='0':
            return 0
        down=1+self.ans(currrow+1,currcol,matrix,row,col)
        right=1+self.ans(currrow,currcol+1,matrix,row,col)
        diag= 1+self.ans (currrow+1,currcol+1,matrix,row,col) 
        
        return min(down,right,diag)
