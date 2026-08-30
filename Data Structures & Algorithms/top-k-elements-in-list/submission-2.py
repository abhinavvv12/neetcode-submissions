class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for num in nums:
            hash_map[num] = hash_map.get(num,0)+1
        sorted_by_value = sorted(hash_map.items(), key=lambda item: item[1], reverse=True)
        ans = []
        for i in range(k):
            ans.append(sorted_by_value[i][0])
        return ans
