class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word3 = ''
        i = 0
        while(i < len(word1) and i < len(word2)):
            word3 = word3 + word1[i] + word2[i]
            i += 1
        if len(word1) > len(word2):
            big = word1
            small = word2 
        else:
            big = word2
            small = word1
        l = len(big) - len(small)
        if( len(word2) == len(word1)):
            return word3
        else:
            word3 = word3 + big[-l:]
            return word3
            
            
        
