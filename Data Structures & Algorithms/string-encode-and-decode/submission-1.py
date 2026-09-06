class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        
        for string in strs:
            encoded_string += "#" + str(len(string)) + "#" + string

        return encoded_string

    def decode(self, s: str) -> List[str]:
        
        index = 0
        finding_length = False
        finding_string = False

        strs = []
        length = 0

        while index < len(s):
            if s[index] == "#" and finding_length == False and finding_string == False:
                finding_length = True
                index += 1
                continue

            if s[index] == "#" and finding_length == True and finding_string == False:
                finding_length = False
                finding_string = True

                if length == 0:
                    strs.append('')
                    finding_string = False

                index += 1
                continue
            
            if finding_length:
                length = (length * 10) + int(s[index])
                index += 1
                continue

            if finding_string:
                strs.append(s[index : index + length])    
                index += length
                length = 0
                finding_string = False
                continue
            
        return strs