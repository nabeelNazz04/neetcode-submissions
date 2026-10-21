class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen={}
        arr=[]
        for i in nums:
            if i not in seen:
                seen[i]=1
            seen[i]+=1
        sorted_arr=(sorted(seen.items(),key=lambda item:item[1],reverse=True))
        count=0
        for num in sorted_arr:
            if count<k:
                arr.append(num[0])
                count+=1
            else:
                break
        return arr
        