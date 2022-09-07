from tkinter import N


class Solution:

    """
        Problem: https://leetcode.com/problems/divide-two-integers/
        Time Taken: 45 min
    """

    def naive_solution(self, dividend: int, divisor: int):
        sign = 1
        if dividend < 0:
            sign *= -1
            dividend *= -1

        if divisor < 0:
            sign *= -1
            divisor *= -1

        current = dividend
        result = 0
        while current > 0:
            result += 1
            current -= divisor

        if current < 0:
            result -= 1

        return result * sign

    def simple_divide(self, dividend, divisor):
        current = dividend
        result = 0
        while current > 0:
            result += 1
            current -= divisor

        if current < 0:
            result -= 1
            current += divisor

        return (str(result), str(current))

    def long_division(self, dividend, divisor):
        sign = 1
        if dividend < 0:
            sign *= -1
            dividend *= -1

        if divisor < 0:
            sign *= -1
            divisor *= -1

        num_str = str(dividend)

        result = ""
        curr = num_str[0]
        index = 1
        while (True):
            curr_num = int(curr)
            if (curr_num >= divisor):
                result_tuple = self.simple_divide(curr_num, divisor)
                result += result_tuple[0]
                curr = result_tuple[1]
            else:
                result += "0"
            
            if (index < len(num_str)):
                curr += num_str[index]
                index += 1
            else:
                break

            
        # For max int safety?
        result = int(result) * sign
        if result > 2147483647:
            result = 2147483647
        elif result < -2147483648:
            result = -2147483648

        return result

    def divide(self, dividend: int, divisor: int) -> int:
        return self.long_division(dividend, divisor)


"""
    # I think this only works in python, where ints are unbound
    def bit_shifting(self, dividend: int, divisor: int) -> int:
        total = 0
		
		# check if we have negative values
        nneg = dividend < 0 
        dneg = divisor < 0

        # base case
        if dividend == divisor:
            return 1
        
		# convert to positive numbers
        dividend = abs(dividend)
        divisor = abs(divisor)
                
		# start from the MSB to prevent arithmetic errors
        for x in range(31, -1, -1):
            shifted = divisor << x
            if shifted <= dividend:
                dividend -= shifted
                total += 1 << x
         
		# if we have opposite signs, the answer is negative
        if nneg != dneg:
            total = -total
        elif total > (1 << 31) - 1: # if the numbers is bigger than 31 bits, e.g. python allows the answer to flow into the 32 bit, then cap it
            total = (1 << 31) - 1
        
        return total
"""

test = Solution()
print(test.divide(-2147483648, -1))