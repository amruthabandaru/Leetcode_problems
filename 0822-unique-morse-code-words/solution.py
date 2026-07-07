class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        mcode=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        result=[]
        for word in words:
            str1=""
            for ch in word:
                str1+=mcode[ord(ch)-97]
            result.append(str1)
        s1=set(result)
        return len(s1)


        \
        
