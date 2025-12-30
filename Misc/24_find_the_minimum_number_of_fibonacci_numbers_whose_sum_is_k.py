# Greedy Approach
class Solution:
    def getClosestFibonacciNumber(self, value: int) -> int:
        first = 0
        second = 1
        third = 1
        while third <= value:
            third = first + second
            first = second
            second = third

        return first

    def findMinFibonacciNumbers(self, k: int) -> int:
        count = 0
        while k:
            k -= self.getClosestFibonacciNumber(
                k
            )  # we will take the closest fibonacci number to k and substract it with k, then use the remaining part of k to repeat the process
            count += 1

        return count
