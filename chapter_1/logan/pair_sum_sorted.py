from typing import List

def pair_sum_sorted(nums: List[int], target: int) -> List[int]:
    # Write your code here
    left = 0
    right = len(nums) - 1
    while left < right:
        mySum = nums[left] + nums[right]
        if mySum == target:
            return [left, right]
        elif mySum < target:
            left += 1
        else:
            right += -1
    return []
 
