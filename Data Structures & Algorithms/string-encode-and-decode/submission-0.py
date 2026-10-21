class Solution:

    def encode(self, strs: List[str]) -> str:
        new_str=""
        for word in strs:
            new_str+=(str(len(word))+"#"+word)
        return new_str
    def decode(self, s: str) -> List[str]:
        result=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1
            word_length=int(s[i:j])
            start_point=j+1
            end_point=start_point+word_length
            word=s[start_point:end_point]
            result.append(word)
            i=end_point
        return result
            