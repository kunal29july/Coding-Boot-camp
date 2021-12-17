'''
You have n dice and each die has k faces numbered from 1 to k.

Given three integers n, k, and target, return the number of possible ways (out of the kn total ways) to roll the dice so the sum of the face-up numbers equals target. Since the answer may be too large, return it modulo 109 + 7.

 

Example 1:

Input: n = 1, k = 6, target = 3
Output: 1
Explanation: You throw one die with 6 faces.
There is only one way to get a sum of 3.
Example 2:

Input: n = 2, k = 6, target = 7
Output: 6
Explanation: You throw two dice, each with 6 faces.
There are 6 ways to get a sum of 7: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
Example 3:

Input: n = 30, k = 30, target = 500
Output: 222616187
Explanation: The answer must be returned modulo 109 + 7.
 

Constraints:

1 <= n, k <= 30
1 <= target <= 1000
Accepted
89.9K
Submissions
189.3K
'''
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        return self.ans(n,k,target,{}) % (10**9 + 7)

    def ans(self,dice,face,target,memo):
        if dice==0 and target!=0:
            return 0
        
        if dice==0 and target==0:
            return 1
        curr_key=(dice,target)
        if curr_key in memo:
            return memo[curr_key]
        ans=0
        for val in range (1,face+1):
            temp=self.ans(dice-1,face,target-val,memo)
            ans=ans+temp 
            memo[curr_key]=ans
        return memo[curr_key]
            
