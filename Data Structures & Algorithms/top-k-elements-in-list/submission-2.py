class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict()
        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] = hashmap[i] + 1

        result = []

        for key, value in dict(sorted(hashmap.items(), key=lambda item: item[1], reverse=True)).items():
            if len(result) < k:
                result.append(key)

        return result