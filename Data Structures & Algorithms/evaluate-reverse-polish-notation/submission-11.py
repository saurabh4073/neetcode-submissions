class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        stack = []
        for s in tokens:
            if s=="+":
                a,b = stack.pop(),stack.pop()
                stack.append(a+b)
            elif s=="-":
                a,b=stack.pop(),stack.pop()
                stack.append(b-a)
            elif s=="*":
                a,b = stack.pop(), stack.pop()
                stack.append(a*b)
            elif s=="/":
                a,b = stack.pop(), stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(s))
        return stack.pop()