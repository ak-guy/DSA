'''
493. Reverse Pairs

Intuition: The intuition behind this solution relies on a divide-and-conquer strategy powered by Merge Sort, 
which transforms a grueling O(N2) brute-force hunt into an efficient O(NlogN) process by counting valid pairs 
while sorting the data. A "reverse pair" occurs when an element appearing earlier in the array is strictly 
greater than twice an element appearing later (L[temp_start]>2*R[ind]). By breaking the array down into smaller, 
independently sorted left (L) and right (R) halves, the algorithm sets up a highly predictable environment: 
because both subarrays are sorted in ascending order, if a number in L is large enough to beat 2*R[ind], 
then every single number following it in L is also guaranteed to beat it. Instead of resetting your search 
for every element in the right subarray, you can use a sliding pointer (temp_start) that only moves forward 
across L. For each element in R, you simply advance temp_start until it hits the first number in L that satisfies 
the condition; at that exact moment, the number of valid pairs contributed by that element is instantly calculated 
as the remaining length of the left array (len(L) - temp_start). By piggybacking this linear pair-counting step 
directly onto the standard merge operation, the algorithm safely measures every cross-boundary relationship before 
physically mixing the arrays together.
'''


class Solution:
    def reversePairs(self, arr: list[int]) -> int:
        n = len(arr)
        return self.merge_sort(arr, 0, n - 1)

    def merge_sort(self, arr: list[int], left: int, right: int) -> int:
        count = 0
        if left < right:
            mid = (left + right) // 2
            count += self.merge_sort(arr, left, mid)
            count += self.merge_sort(arr, mid + 1, right)
            count += self.merge(arr, left, mid, right)
        return count

    def merge(self, arr: list[int], left: int, mid: int, right: int) -> int:
        L = arr[left : mid + 1]
        R = arr[mid + 1 : right + 1]

        # Calculating reverse pairs
        count = 0
        temp_start = 0
        for ind in range(len(R)):
            while temp_start < len(L) and R[ind] * 2 >= L[temp_start]:
                temp_start += 1
            count += len(L) - temp_start

        # Merging the sorted arrays back into the original array
        i, j, k = 0, 0, left
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Copy remaining elements of L, if any
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        # Copy remaining elements of R, if any
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

        return count
