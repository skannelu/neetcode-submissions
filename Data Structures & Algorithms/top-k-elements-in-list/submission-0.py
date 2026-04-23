class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # solution 1 ============
        # hmap = {}
        # for i, num in enumerate(nums):
        #     hmap[num] = 1 + hmap.get(num, 0)

        # arr = []
        # for j in hmap:
        #     if k <= hmap[j]:
        #         arr.append(j)

        # return arr
        # solution 2 ==========
        # hmap = {}
        # for num in nums:
        #     hmap[num] = 1 + hmap.get(num, 0)
        
        # arr = []
        # for num, cnt in hmap.items():
        #     arr.append([cnt, num])
        # arr.sort()

        # res = []
        # while len(res) < k:
        #     res.append(arr.pop()[1])
        # return res
        # solution 3 min heap =============
        # hmap = {}
        # for num in nums:
        #     hmap[num] = 1 + hmap.get(num, 0)
        
        # heap = []
        # for num in hmap.keys():
        #     heapq.heappush(heap, (hmap[num], num))
        #     if len(heap) > k:
        #         heapq.heappop(heap)
        # res = []
        # for i in range(k):
        #     res.append(heapq.heappop(heap)[1])
        # return res
        # solution 4 bucket sort ============
        hmap = {}
        for num in nums:
            hmap[num] = 1 + hmap.get(num, 0)
        freq = [[] for i in range(len(nums) + 1)]
        for num, cnt in hmap.items():
            freq[cnt].append(num)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res