class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openbrack = {'{': '}', '(':')', '[':']'}
        for char in s:
            if char in openbrack:
                stack.append(openbrack[char])
            elif len(stack) and stack.pop() == char:
                continue
            else:
                print("s",stack)
                return False
        return len(stack)==0