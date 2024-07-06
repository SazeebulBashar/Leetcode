class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cycles = time // (n-1)
        remainder = time % (n-1)
        return 1+remainder if cycles % 2==0 else n-remainder