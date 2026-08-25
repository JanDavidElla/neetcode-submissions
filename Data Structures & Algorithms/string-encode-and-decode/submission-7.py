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
        for i in range(len(s)):
        

            if counting:
                if s[i] == "#": 
                    count = int(count)
                    wordList.append("")
                    counting = False
                else:
                    count += s[i]
            else:
                if count == 0:
                    counting = True
                    count = "" + s[i]
                    index = 0
                else:

                    wordList[-1] += s[i]
                    index += 1
                    
                    if index == count:
                        counting = True
                        count = ""
                        index = 0
                
        return wordList


            
            
            
