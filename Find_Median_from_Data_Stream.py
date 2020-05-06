# https://leetcode.com/problems/find-median-from-data-stream/
import bisect
class MedianFinder:

    def __init__(self):
        self.arr = []
        self.length = 0

    def addNum(self, num: int) -> None:
        bisect.insort(self.arr, num) # appaned num while maintaining numeric order
        self.length += 1

    def findMedian(self) -> float:
        if self.length % 2 != 0:
            return self.arr[self.length//2]
        else:
            return (self.arr[(self.length//2) - 1] + self.arr[self.length//2]) / 2
