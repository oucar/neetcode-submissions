class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        closing_to_opening = {
            ']' : '[',
            ')' : '(',
            '}' : '{',
        }


        for char in s:
            is_closing_bracket = char in closing_to_opening 

            if is_closing_bracket:
                if len(stack) == 0:
                    return False
            
                expected = closing_to_opening[char]
                most_recent = stack[-1]

                if most_recent != expected:
                    return False
                
                stack.pop()

            else: 
                stack.append(char)

        if len(stack) == 0:
            return True
        else:
            return False
