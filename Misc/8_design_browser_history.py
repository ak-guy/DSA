class BrowserHistory:
    def __init__(self, homepage: str):
        self.homepage = homepage
        self.st = []
        self.st.append(homepage)
        self.st_len = 1
        self.loc = 1

    def visit(self, url: str) -> None:
        while self.loc < self.st_len:
            self.st_len -= 1
            self.st.pop()
        self.st.append(url)
        self.st_len += 1
        self.loc = self.st_len

    def back(self, steps: int) -> str:
        if steps < self.loc:
            self.loc -= steps
        else:
            self.loc = 1
        return self.st[self.loc - 1]

    def forward(self, steps: int) -> str:
        if steps < self.st_len - self.loc:
            self.loc += steps
        else:
            self.loc = self.st_len
        return self.st[self.loc - 1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
