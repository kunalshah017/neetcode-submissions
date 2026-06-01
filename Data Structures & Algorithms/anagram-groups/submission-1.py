class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = {}

        for string in strs:
            x = "".join(sorted(string))

            if x not in hashmap:
                hashmap[x] = []

            hashmap[x].append(string)

        return list(hashmap.values())