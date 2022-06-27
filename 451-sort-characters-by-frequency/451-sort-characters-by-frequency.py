class Solution:
    def frequencySort(self, s: str) -> str:
        hash_map = {}
        n = len(s)
        
        for i in range(n):
            if s[i] not in hash_map:
                hash_map[s[i]] = 1
            
            else:
                hash_map[s[i]] += 1

        ans = ""
        res = []
        for k,v in hash_map.items():
            res.append([k,v])
        
        res = sorted(res, key = lambda x:x[1] , reverse= True)
        
        # print(res)
        
        for ele in res:
            ans += ele[1] * ele[0]
            
            
        return ans
        
        