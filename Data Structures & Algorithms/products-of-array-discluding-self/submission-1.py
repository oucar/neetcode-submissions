class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        running = 1
        for i in range(n):
            answer[i] = running
            running = running * nums[i]

        running = 1
        # python range never includes the stopping
        # so it's -1 instead of 0
        for i in range(n - 1, -1, -1):
            answer[i] = answer[i] * running
            running = running * nums[i]

        return answer