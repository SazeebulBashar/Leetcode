class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res=[0,0]
        count = collections.Counter(nums)
        # [duplicate, missing]
        for i in range(1,len(nums)+1):
            if count[i] == 0:
                res[1]=i
            if count[i] == 2:
                res[0]=i

        return res