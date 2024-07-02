class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # Solution 1

        result =[]
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                result.append(nums1[i])
                nums2.remove(nums1[i])
        return result


        # Solution 2

        nums1.sort()
        nums2.sort()
        i,j=0,0
        result=[]
        while i < len(nums1) and j < len(nums2):
            if nums1[i]  ==  nums2[j]:
                result.append(nums1[i])
                i+=1
                j+=1
            elif nums1[i] < nums2[j]:
                i+=1
            else:
                j+=1
        return result