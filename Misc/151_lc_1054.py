'''
1054. Distant Barcodes
'''

'''
This solution rearranges the input barcodes so that no two adjacent 
elements are the same by using a max-heap based on the frequency of
each barcode. First, it counts the occurrences of each barcode 
and pushes them into a max-heap with negative counts for easy access 
to the most frequent barcodes. Then, it repeatedly pops the two most 
frequent barcodes, appends them to the result while ensuring the newly 
added barcode is not the same as the previously added one, and pushes 
any remaining counts back into the heap. This process continues until 
one or no barcodes remain, with the leftover barcode appended at the 
end, ensuring a valid arrangement is returned.
'''

import heapq
from typing import List
from collections import defaultdict
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        hq = []

        barcode_count_mapping = defaultdict(int)
        for val in barcodes:
            barcode_count_mapping[val] += 1
        
        for key, val in barcode_count_mapping.items():
            heapq.heappush(hq, (-val, key))

        result = []
        while len(hq) > 1:
            first_count, first_val = heapq.heappop(hq)
            second_count, second_val = heapq.heappop(hq)

            if result:
                if result[-1] == first_val:
                    result.append(second_val)
                    if second_count+1 != 0:
                        heapq.heappush(hq, (second_count+1, second_val))
                    heapq.heappush(hq, (first_count, first_val))
                else:
                    result.append(first_val)
                    if first_count+1 != 0:
                        heapq.heappush(hq, (first_count+1, first_val))
                    heapq.heappush(hq, (second_count, second_val))
            else:
                result.append(first_val)
                if first_count+1 != 0:
                    heapq.heappush(hq, (first_count+1, first_val))
                heapq.heappush(hq, (second_count, second_val))
        
        # handle the last barcode in heap
        count, val = heapq.heappop(hq)
        result.append(val)
        
        return result
