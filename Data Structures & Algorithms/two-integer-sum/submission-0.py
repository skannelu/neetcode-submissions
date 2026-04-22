class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # solution 1 ======
        # for i in range(len(nums)):
        #     for j in range( i+1, len(nums)):
        #         if i != j and nums[i] + nums[j] == target:
        #             return [i, j]
            
        # return []
        # solution 2 =======
        # nums_copy = []
        # for i, num in enumerate(nums):
        #     nums_copy.append([num, i])
        
        # nums_copy.sort()
        # i = 0
        # j = len(nums) - 1
        # while i < j:
        #     if nums_copy[i][0] + nums_copy[j][0] == target:
        #         return [min(nums_copy[i][1], nums_copy[j][1]), max(nums_copy[i][1], nums_copy[j][1])]
        #     elif nums_copy[i][0] + nums_copy[j][0] < target:
        #         i = i + 1
        #     else:
        #         j = j - 1
        # return []
        # solution 3 ===============
        hmap = {} # [3,4,5,6] 7
        for i, num in enumerate(nums):
            if target - num in hmap and hmap[target - num] != i:
                return [min(i, hmap[target - num]), max(i, hmap[target - num])]
            else:
                hmap[num] = i
        return []