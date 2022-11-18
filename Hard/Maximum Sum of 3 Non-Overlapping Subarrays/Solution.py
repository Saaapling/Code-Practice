class Solution:
    
    """
        Problem: https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/
        Comments: 
            - Initial Thoughts: Triple Iteration + end processing
                - Post Submission: This does NOT work. Only works for k=2,3
                    -Theoretically, O(N) solutions
            - Optimal Solution: O(N)
                - Assuming you have a magic box that gives you best subarr from arr[:i] and arr[j:]
                    - This operation finishes in O(1)
                    - This can be done by precomputing in O(n) time
                - You only need to find the best index to split the array (best middle subarr)
                - Compare ~n middle subarrays with constant O(1) lookup for its best end subarrs
                - Courtesy of Erik
    """
    
    def incorrect_iterative(self, nums, k):
        found = []
        
        def get_range(nums, k):
            cs = 0
            i = 0
            while nums[i] < 0:
                i += 1
            
            l = i
            found = 0
            while found < k:
                if nums[i] > 0:
                    cs += nums[i]
                    found += 1
                i += 1
                
            ms = cs
            sa_range = (l, i-1)
            for i in range(i, len(nums)):
                if nums[i] < 0:
                    continue
                    
                cs += (nums[i] - nums[l])
                l += 1
                while nums[l] < 0:
                    l += 1
                if cs > ms:
                    ms = cs
                    sa_range = (l, i)
        
            for idx in range(sa_range[0], sa_range[1] + 1):
                nums[idx] = -1
        
            return sa_range
        
        for i in range(3):
            found.append(get_range(nums, k))
        found.sort()
        
        # print(found)
        # print(nums)
        
        # Merge Arrays:
        i = 0
        while i < len(found)-1:
            if found[i][1] > found[i+1][0]:
                found.pop(i+1)
            else:
                i += 1
        
        # print(found)
        ans = []
        for i in found:
            for j in range(i[0], i[1]+1, k):
                ans.append(j)
                
        return ans
    
    
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        f2b = [-1 for _ in range(n)]
        b2f = [-1 for _ in range(n)]
        sas = [-1 for _ in range(n)]
        
        fsum = 0
        bsum = 0
        for i in range(k):
            fsum += nums[i]
            bsum += nums[~i]
            
        fmv = fsum
        bmv = bsum
        f2b[0] = (fmv, 0)
        b2f[-k] = (bmv, n-k)
        sas[0] = fsum
        for i in range(n-k):
            idx = i + k
            fsum += nums[idx] - nums[i]
            bsum += nums[~idx] - nums[~i]
            
            sas[i+1] = fsum
            if fsum > fmv:
                fmv = fsum
                f2b[i+1] = (fmv, i+1)
            else:
                f2b[i+1] = f2b[i]
                
            if bsum >= bmv:
                bmv = bsum
                b2f[-(idx+1)] = (bmv, n-idx-1)
            else:
                b2f[-(idx+1)] = b2f[-(idx)]
               
        # print(sas)
        # print(f2b)
        # print(b2f)
        
        mv = 0
        ans = [-1, -1, -1]
        for i in range(k, n-2*k + 1):
            curr = sas[i] + f2b[i-k][0] + b2f[i+k][0]
            if curr > mv:
                mv = curr
                ans = [f2b[i-k][1], i, b2f[i+k][1]]
            
        # print(mv)
        return ans