class Solution:
    
    """
        Problem: https://leetcode.com/contest/weekly-contest-248/problems/count-good-numbers/
        Comments: Fermat's not needed, use binary decomposition
        Eric's method:
            def countGoodNumbers(self, n: int) -> int: 
                M = 10**9+7
                odds = n//2
                evens = ceil(n/2)
                def pwr(b, N): #efficiently compute b**N
                    dp = [b]
                    for k in range(1, 64):
                        dp.append(dp[-1] ** 2 % M)
                    ans = 1
                    for k in range(64):
                        if N & 1 << k: 
                            N &= ~(1 << k)
                            ans = (ans * dp[k]) % M
                            if not N: 
                                break
                    return ans
                return (pwr(4, odds) * pwr(5, evens)) % M
    """
    
    def attempted_solution_1(self, n):
        if n == 1:
            return 5
        elif n == 2:
            return 20
        
        dp_arr = [0] * (n+3)
        dp_arr[1] = 5
        dp_arr[2] = 20
        
        for i in range(3, n+1, 2):
            dp_arr[i] = (dp_arr[i-1] * 5) % (math.pow(10,9) + 7)
            dp_arr[i+1] = (dp_arr[i] * 4) % (math.pow(10,9) + 7)
        
        if i == n:
            dp_arr[i] = (dp_arr[i-1] * 5) % (math.pow(10,9) + 7)
        
        return int(dp_arr[n])
    
    def attempted_solution_2(self, n):
        last = 5
        index = 1
        sign = 1
        
        while index < n:
            if sign:
                last = (last * 4) % (math.pow(10,9) + 7)
            else:
                last = (last * 5) % (math.pow(10,9) + 7)
            sign *= -1
            index += 1
    
        return last
    
    def countGoodNumbers(self, n: int) -> int:
        # Have to use math to sorten this
        """
            Number of (*5) = n/2 + (n%2)
            Number of (*4) = n/2
            Apply Fermat's Little Theorem: https://www.geeksforgeeks.org/fermats-little-theorem/
            Abuse python's large ints
        """
        b = int(n/2) # 4's
        a = b + (n%2) # 5's

        # Fermat's little theorem
        a = a % (math.pow(10,9) + 6)
        b = b % (math.pow(10,9) + 6)

        print(a)
        print(b)

        # Not a Great method
        temp = 1
        while a > 20:
            a -= 20
            temp = (temp * (math.pow(5, 20) % (math.pow(10,9) + 7))) % (math.pow(10,9) + 7)
        a = (temp * (math.pow(5, a) % (math.pow(10,9) + 7))) % (math.pow(10,9) + 7)

        temp = 1
        while b > 20:
            b -= 20
            temp = (temp * (math.pow(4, 20) % (math.pow(10,9) + 7))) % (math.pow(10,9) + 7)
        b = (temp * (math.pow(4, b) % (math.pow(10,9) + 7))) % (math.pow(10,9) + 7)

        return int((a * b) % (math.pow(10,9) + 7))
        