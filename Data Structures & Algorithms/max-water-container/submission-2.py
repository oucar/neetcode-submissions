class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left, right = 0, len(heights) - 1
        best = 0

        while left < right:
            # diff * the short one 
            width = abs(left - right)
            area = width * min(heights[left], heights[right])
            best = max(best, area)

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return best 