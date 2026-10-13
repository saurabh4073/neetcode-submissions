class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i,a in enumerate(temperatures):
            while stack and stack[-1][0]<a:
                stacka,stacki = stack.pop()
                res[stacki]=i-stacki
            stack.append([a,i])
        return res