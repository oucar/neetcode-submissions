class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        output = [0] * len(temperatures)
        stack = [] # pair: [temp, index]

        for i, temp in enumerate(temperatures):
            # top of stack --> [temp, index]
            while stack and stack[-1][0] < temp:
                stackTemp, stackIndex = stack.pop()
                output[stackIndex] = (i - stackIndex)
            stack.append([temp, i])
        return output


