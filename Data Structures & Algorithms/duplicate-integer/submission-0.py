class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newNums = sorted(nums)
        for i in range(len(newNums)-1):
            if newNums[i] == newNums[i+1]:
                return True
        return False
            
        