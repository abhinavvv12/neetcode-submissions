class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_count = 0
        for num in nums:
            count = 0
            if num-1 in num_set:
                continue
            if num+1 in num_set:
                i = 1
                len = 0
                while num+i in num_set :
                    count+=1
                    i+=1
            max_count = max(count, max_count)
        return 0 if nums==[] else max_count+1