#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        
        if k > n:
            k = k % n
        
        nums[:] = nums[n - k:] + nums[:n - k]
        
# @lc code=end

