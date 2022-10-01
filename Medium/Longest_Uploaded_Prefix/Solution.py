class LUPrefix:

    def __init__(self, n: int):
        self.uploaded = [False] * (n+2)
        self.prefix = 1

    def upload(self, video: int) -> None:
        self.uploaded[video] = True
        while self.uploaded[self.prefix]:
            self.prefix += 1

    def longest(self) -> int:
        return self.prefix - 1
        


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()