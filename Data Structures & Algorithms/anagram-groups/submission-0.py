from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []

        for string in strs:
            found = False
            
            for ana_strs in output:
                if Counter(list(string)) == Counter(list(ana_strs[0])):
                    ana_strs.append(string)
                    found = True
            
            if not found:
                output.append([string])
        
        return output