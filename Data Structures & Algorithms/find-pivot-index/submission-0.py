class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = []
        postfix = []

        runningSum = 0
        for i, n in enumerate(nums):
            prefix.append(runningSum)
            runningSum += n

        runningSum = 0
        for i in range(len(nums) -1, -1, -1):
            postfix.append(runningSum)
            runningSum += nums[i]

        postfix.reverse()

        for i, n in enumerate(prefix):
            if prefix[i] == postfix[i]:
                return i
        return -1