class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        output = [0] * len(temperatures)
        stack = [] # stores the index 

        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prev = stack.pop()
                output[prev] = i - prev
            stack.append(i)
        return output


