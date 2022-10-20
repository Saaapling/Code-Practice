class Solution:
    
    """
        Problem: https://leetcode.com/problems/integer-to-roman/submissions/
        Comments: Glorified if-statement, not a big fan of this question/solution
            - Other slightly cleaner methods: https://leetcode.com/problems/integer-to-roman/solution/
    """
    
    def intToRoman(self, num: int) -> str:
        if num >= 1000:
            return "M" + self.intToRoman(num - 1000)
        elif num >= 100:
            if num >= 900:
                return "CM" + self.intToRoman(num - 900)
            elif num >= 500:
                return "D" + self.intToRoman(num - 500)
            elif num >= 400:
                return "CD" + self.intToRoman(num - 400)
            else:
                return "C" + self.intToRoman(num-100)
        elif num >= 10:
            if num >= 90:
                return "XC" + self.intToRoman(num - 90)
            elif num >= 50:
                return "L" + self.intToRoman(num - 50)
            elif num >= 40:
                return "XL" + self.intToRoman(num - 40)
            else:
                return "X" + self.intToRoman(num-10)
        elif num > 0:
            if num == 9:
                return "IX"
            elif num >= 5:
                return "V" + self.intToRoman(num - 5)
            elif num == 4:
                return "IV"
            else:
                return "I" + self.intToRoman(num-1)
            
        return ""