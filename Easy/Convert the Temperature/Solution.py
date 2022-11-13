class Solution:
    
    """
        Problem: https://leetcode.com/contest/weekly-contest-319/problems/convert-the-temperature/
    """
    
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius + 273.15, celsius * 1.80 + 32.00]
        