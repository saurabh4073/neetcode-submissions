class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openbrac = {'{':'}',
        '[':']',
        '(':')'
        }

        for char in s:
            if char in openbrac:
                stack.append(openbrac[char])
            elif stack and stack.pop() == char:
                continue
            else:
                return False
        return len(stack)==0
            
