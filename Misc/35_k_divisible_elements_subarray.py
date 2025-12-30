# # using python hash function gives wrong answer
from typing import List


class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        ans_set = set()
        for i in range(len(nums)):
            cnt_one = 0
            for j in range(i, len(nums)):
                concatenate_int_to_string_val = "".join(map(str, nums[i : j + 1]))
                new_hash = hash(concatenate_int_to_string_val)
                if nums[j] % p == 0:
                    cnt_one += 1
                if cnt_one <= k:
                    ans_set.add(new_hash)
                else:
                    break

        return len(ans_set)


# # using custom hash calculator gives successful submission
class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        ans_set = set()
        mod = 100000000069
        for i in range(len(nums)):
            cnt_one = 0
            dummy_hash = 0
            for j in range(i, len(nums)):
                # creating hash value based on the value present at jth index and the length of subarray
                dummy_hash = ((dummy_hash * 193) + nums[j] + j - i + 1) % mod
                if nums[j] % p == 0:
                    cnt_one += 1
                if cnt_one <= k:
                    ans_set.add(dummy_hash)
                else:
                    break

        return len(ans_set)
