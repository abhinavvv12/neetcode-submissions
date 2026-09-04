class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = len(nums)-1
        idx =0
        while idx<=j:
            if nums[idx] == 0:
                nums[i],nums[idx]=nums[idx],nums[i]
                i+=1
                idx+=1
            elif nums[idx] == 2:
                nums[j],nums[idx] = nums[idx],nums[j]
                j-=1
            else:
                idx+=1
        return nums

        