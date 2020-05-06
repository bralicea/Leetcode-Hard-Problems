# https://leetcode.com/problems/first-missing-positive/
import bisect
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums_noreps = []
        for num in nums:
            if num not in nums_noreps and num > 0:
                bisect.insort(nums_noreps, num)

        if nums_noreps == []:
            return 1

        for cnt,num in enumerate(nums_noreps, 1):
            if cnt != num:
                return cnt
        return cnt + 1
