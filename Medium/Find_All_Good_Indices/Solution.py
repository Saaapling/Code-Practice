class Solution:
    
    
    """
        Problem: https://leetcode.com/contest/weekly-contest-312/problems/find-all-good-indices/
        Comments: [1,2,3,1,3,4,1,2]
            Iterative with saved previous stuff:
                - Case: previous element (n-1) is good:
                    - for next element (n), check (n-2) > (n-1) and (n+k) > (n+k-1)
                - Case: previous element (n-1) i BAD!
                    - if left is bad: 
            Precalculate length of subarray that is increasing or decreasing:
                    [2,1,1,1,3,4,1] -> [0,-2,0,0,4,5,-2]
                    for i = 2, check arr[i-1], arr[i+k]
                        arr[i-1] <= k
                        arr[i+k] >= k
                        if arr[n] == 0, go to prev non-zero element
            Post Submission: Times Out
    
    """
    
    def goodIndices_TLE(self, nums: list[int], k: int) -> list[int]:
        if len(nums) <= 2*k:
            return []
        
        if k == 1:
            return list(range(k,len(nums)-k))
        
        id_arr = [0] * len(nums)
        prev = nums[0]
        prev_index = 0
        
        
        
        for i in range(1, len(nums)):
            if nums[i] == prev:
                id_arr[i] = 0
            elif nums[i] < prev:
                if id_arr[prev_index] < 0:
                    id_arr[i] += id_arr[prev_index] - (i - prev_index)
                else:
                    id_arr[i] = -1 - (i - prev_index)
                prev = nums[i]
                prev_index = i
            else:
                if id_arr[prev_index] > 0:
                    id_arr[i] += id_arr[prev_index] + (i - prev_index)
                else:
                    id_arr[i] = 1 + (i - prev_index)
                prev = nums[i]
                prev_index = i
                
        #print(id_arr)
        
        result = []
        for i in range(k, len(nums) - k):
            curr = id_arr[i]
            if id_arr[i-1] != 0:
                if id_arr[i-1] > (k * -1):
                    continue 
            else:
                count = 1
                temp = i - 2
                while count < k and id_arr[temp] == 0:
                    count += 1
                    temp -= 1
                if count < k:
                    if id_arr[temp] - count > (k * -1):
                        continue
            
            if id_arr[i+k] != 0:
                if id_arr[i+k] < k:
                    continue
            else:
                count = 1
                temp = i + k - 1
                while count < k and id_arr[temp] == 0:
                    count += 1
                    temp -= 1
                if (count+1) < k:
                    if id_arr[temp] + count < k:
                        continue
                        
            result.append(i)
            
        return result
    
    def goodIndices(self, nums: list[int], k: int) -> list[int]:
        if len(nums) <= 2*k:
            return []
        
        if k == 1:
            return list(range(k,len(nums)-k))
        
        asc_arr = [1] * len(nums)
        desc_arr = [1] * len(nums)
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                asc_arr[i] = asc_arr[i-1] + 1
                desc_arr[i] = desc_arr[i-1] + 1
            elif nums[i] < nums[i-1]:
                asc_arr[i] = 1
                desc_arr[i] = desc_arr[i-1] + 1
            else:
                asc_arr[i] = asc_arr[i-1] + 1
                desc_arr[i] = 1

        # print(asc_arr)
        # print(desc_arr)

        result = []
        for i in range(k, len(nums) - k):
            if desc_arr[i-1] < k:
                continue 
            if asc_arr[i+k] - asc_arr[i+1] != k - 1:
                continue
            result.append(i)
            
        return result
        
test = Solution()
input = [1,2,3,1,3,4,1,2]
k = 2
result = test.goodIndices(input, k)
print(result)