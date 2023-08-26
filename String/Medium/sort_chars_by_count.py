import heapq
class Solution:
    def frequencySort(self, s: str) -> str:
        count_array = [[0,i] for i in range(62)] # to maintain count of all 62 chars
        unique_elem = set()
        pq = []
        # A(0) to Z(25) then a(26) to z(51) then 0(52) to 9(61)

        # ord('A') = 65 and ord('a') = 97
        for char in s:
            if char.isupper():
                count_array[25 - (ord('Z') - ord(char))][0] -= 1
            elif char.islower():
                count_array[51 - (ord('z') - ord(char))][0] -= 1
            else:
                count_array[52 + int(char)][0] -= 1
            unique_elem.add(char)

        for i in range(62):
            heapq.heappush(pq, count_array[i])

        res = ''
        for i in range(len(unique_elem)):
            count, ind = heapq.heappop(pq)
            if ind < 26:
                res += chr(65+ind)*(-count)
            elif ind < 52:
                res += chr(97-26+ind)*(-count)
            else:
                res += str(ind - 52) * (-count)
                   
        return res