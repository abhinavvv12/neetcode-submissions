class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cnt = nums.count(val)
        while cnt!=0:
            nums.remove(val)
            cnt-=1
        return len(nums)