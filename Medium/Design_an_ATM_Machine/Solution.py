class ATM:

    """
        Problem: https://leetcode.com/contest/biweekly-contest-76/problems/design-an-atm-machine/
    """

    def __init__(self):
        self.notes = [0,0,0,0,0]
        self.bnv = [20,50,100,200,500]
        

    def deposit(self, banknotesCount: list[int]) -> None:
        for i in range(len(banknotesCount)):
            self.notes[i] += banknotesCount[i]
        

    def withdraw(self, amount: int) -> List[int]:
        bnw = [0,0,0,0,0]
        idx = 4
        while idx >= 0:
            val = self.bnv[idx]
            
            bnc = amount // val
            if bnc > self.notes[idx]:
                bnw[idx] += self.notes[idx]
                amount -= val * self.notes[idx]
            else:
                bnw[idx] += bnc
                amount -= val * bnc
                
            idx -= 1
        
        if amount != 0:
            return [-1]
                
        for i in range(len(bnw)):
            self.notes[i] -= bnw[i]
                
        return bnw
                


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)