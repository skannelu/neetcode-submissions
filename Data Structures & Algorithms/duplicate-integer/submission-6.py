class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        # solution 1 ========
        # for i in range(len(nums)):
        #     if i+1 < len(nums) and nums[i] == nums[i+1]:
        #         return True
        #     else:
        #         continue   
        # return False
        # =================
        # solution 2 =======
        # hash set
        numsset = set()
        for num in nums:
            if num in numsset:
                return True
            numsset.add(num)            
        return False
        # ==================
        # solution 3 ========
        # dictionary
        # numsset = dict()
        # for num in nums:
        #     if num in numsset:
        #         return True
        #     numsset[num] = 1
        # return False
        