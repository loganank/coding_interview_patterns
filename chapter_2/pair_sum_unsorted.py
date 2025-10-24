from typing import List

def pair_sum_unsorted(nums: List[int], target: int) -> List[int]:
    map = {}
    for i in range(len(nums)):
        map[nums[i]] = i
    for i in range(len(nums)):
        compliment = target - nums[i]
        # compliment in map and not same index as current number
        if compliment in map and map[compliment] != i:
            return [i, map[compliment]]

    # base case
    return []
