import math

class Solution:

    """
        Problem: https://leetcode.com/problems/count-special-integers/
        Time Taken: ~45 min
        Comments: 'Math' solution (not really DP)
            - The maximum distinct number is 9876543210
            - Set number of n digit distinct numbers: 9 * 9! / (9-n+1)! [9 * 9 * 7 * 6 * 1] / []
            - The number of distinct numbers less a digit of n-length where the first digit is k is:
                    - number of 1 to (n-1) digit distinct numbers plus
                    - for j from (1-k): non-inclusive for k
                        - plus (n-1) digit distinct numbers w/o the starting digit (9! / (9 - n + 1)!
                    - For the kth: (recurse the above?)
                        - keep track of already seen digits, break if repeat
        Post-Submission Comments:
            - The math method absolute works, and performs very well. In fact, it can be improved bc
                    there are many repeat operations
            - There is also a DP solution with bitmask, but the 'math' version seems better, thus, exempted for this
    """
    def countSpecialNumbers_improved(self, n: int) -> int:
        count = 0
        num_array = [int(x) for x in str(n)]
        length = len(num_array)


        # Add the distinct numbers with 1 to (length-1) digits
        for x in range(1, length):
            count += 9 * math.factorial(9) / math.factorial(9 - (x - 1))

        print(count)

        seen = set()
        first = True
        for x in num_array:
            length -= 1

            if first:
                first = False
                count += ((x - 1) - len(seen)) * (math.factorial(9) / math.factorial(9 - length))
                print('a')
            else:
                remaining = 10 - len(seen) - 1
                j = 0
                for i in range(0, x):
                    if i in seen:
                        j += 1
                count += (x - j) * (math.factorial(remaining) / math.factorial(remaining - length))
                print('b')

            print(count)

            if x in seen:
                return int(count)

            seen.add(x)

        if length == 0:
            count += 1

        return int(count)

    def countSpecialNumbers(self, n: int) -> int:
        count = 0
        num_array = [int(x) for x in str(n)]
        length = len(num_array)


        # Add the distinct numbers with 1 to (length-1) digits
        for x in range(1, length):
            count += 9 * math.factorial(9) / math.factorial(9 - (x - 1))

        print(count)

        seen = set()
        first = True
        for x in num_array:
            length -= 1

            if first:
                first = False
                for i in range(1, x):
                    if i in seen:
                        continue
                    count += (math.factorial(9) / math.factorial(9 - length))
                    print('a')
            else:
                for i in range(0, x):
                    remaining = 10 - len(seen) - 1
                    if i in seen:
                        continue
                    count += (math.factorial(remaining) / math.factorial(remaining - length))
                    print('b')
            
            print(count)

            if x in seen:
                length += 1
                break
            seen.add(x)

        if length == 0:
            count += 1

        return int(count)


test = Solution()
input = 135
result = test.countSpecialNumbers_improved(input)
print(result)