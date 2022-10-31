from collections import defaultdict

class Solution:
    
    """
        Problem: https://leetcode.com/contest/weekly-contest-317/problems/most-popular-video-creator/
    """
    
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        val = defaultdict(lambda:[0,-1,""])
        n = len(ids)
        
        for i in range(n):
            val[creators[i]][0] += views[i]
            if val[creators[i]][1] == views[i]:
                val[creators[i]][2] = min(val[creators[i]][2], ids[i])
            else:
                if val[creators[i]][1] < views[i]:
                    val[creators[i]][1] = views[i]
                    val[creators[i]][2] = ids[i]
                    
        for key in val:
            val[key].append(key)
                    
        x = list(val.values())
        x.sort(reverse = True)
        # print(x)
        
        count = x[0][0]
        i = 0
        res = []
        while i < len(x) and x[i][0] == count:
            res.append([x[i][3],x[i][2]])
            i += 1
            
        return res