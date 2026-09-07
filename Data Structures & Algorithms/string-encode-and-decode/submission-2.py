class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        
        for string in strs:
            encoded_string += str(len(string)) + "#" + string

        return encoded_string

    def decode(self, s: str) -> List[str]:
        
        i = 0
        strs = []
        length = 0

        while i < len(s):
            
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            strs.append(s[j + 1 : j + length + 1])

            i = j + length + 1

        return strs