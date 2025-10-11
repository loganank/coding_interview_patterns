from typing import List

def shift_zeros_to_the_end(nums: List[int]) -> None:
    left = 0

    for i in range(len(nums)):
        if nums[left] != 0:
            left += 1

    right = left + 1
    # go from left to right moving non zeros to left most spot
    while right < len(nums):
        # if you find a zero, move it to the right
        if nums[left] != 0:
            left += 1
            if right == left:
                right += 1
        elif nums[right] == 0:
            right += 1
        else:
            # left value is non zero, right value is zero
            # swap
            nums[left] = nums[right]
            nums[right] = 0
            left += 1
            right += 1
