# https://leetcode.com/problems/median-of-two-sorted-arrays/
from statistics import median

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return median(nums1 + nums2)
