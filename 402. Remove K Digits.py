class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack =[]
        ans=[]
        for c in num:
            while stack and k>0 and stack[-1] > c:
                k-=1
                stack.pop()
            stack.append(c)
        stack = stack[:len(stack)-k]
        for c in stack:
            if c=='0' and not ans:
                continue
            ans.append(c)
        res = "".join(ans)

        return res if ans else '0'


            

