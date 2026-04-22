class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # solution 1 hash map ===============
        # hmap = {}
        # for i, strEl in enumerate(strs):
        #     sorted_copy_str = "".join(sorted(strEl))
        #     if sorted_copy_str in hmap:
        #         hmap[sorted_copy_str].append(strEl)
        #     else:
        #         hmap[sorted_copy_str] = [strEl]
        # return list(hmap.values())
        # solution 2 ===================
        hmap = defaultdict(list)
        for i, strEl in enumerate(strs):
            count = [0] * 26
            for c in strEl:
                count[ord(c) - ord('a')] += 1
            hmap[tuple(count)].append(strEl)
        return list(hmap.values())
