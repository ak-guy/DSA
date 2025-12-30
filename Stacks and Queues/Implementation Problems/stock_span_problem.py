class StockSpanner:
    """
    we will create a monotonic decreasing stack which will have [val, count]
    count -> no of consecutive days for which it was increasing
    """

    def __init__(self):
        self.st = []

    def next(self, price: int) -> int:
        res = 1
        while self.st and self.st[-1][0] <= price:
            res += self.st[-1][1]
            self.st.pop()
        self.st.append([price, res])
        return res
