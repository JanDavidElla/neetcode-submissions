class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        start with empty array (output)
        for loop 
        """
        output = {}
        for word in strs:
            insert = False
            anagramed = tuple(sorted(list(word)))
            if anagramed in output.keys():
                output[anagramed].append(word)
                insert = True
                continue
            if not insert:
                output[anagramed] = [word]
        return list(output.values())
            
                
