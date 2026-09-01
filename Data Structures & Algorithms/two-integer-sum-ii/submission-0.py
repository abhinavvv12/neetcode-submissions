class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans = []
        i = 0
        j = 1

        while i<=j:
            if numbers[i]+numbers[j] == target and i!=j:
                return [i+1,j+1]
            elif numbers[i]+numbers[j] < target:
                i+=1
                j+=1
            else:
                return [-1,-1]


        
        