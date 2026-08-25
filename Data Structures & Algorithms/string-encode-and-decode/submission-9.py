class Solution:

    def encode(self, strs: List[str]) -> str:
        word = ""
        for element in strs:
            word += str(len(element)) + "#" + element
        print(word)
        return word

    def decode(self, s: str) -> List[str]:
        wordList = []
        count = ""
        index = 0
        counting = True

        i = 0
        while i < len(s):
            j = i #count
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])
            i = j + 1
            wordList.append(s[i:i + length])
            i += length

        return wordList


            
            
            
