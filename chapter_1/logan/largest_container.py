from typing import List

def largest_container(heights: List[int]) -> int:
    left = 0
    right = len(heights) - 1
    largest = 0
    while left < right:
        area = (right - left) * min(heights[left], heights[right])
        largest = max(largest, area)
        if heights[left] < heights[right]:
            left += 1
        elif heights[left] > heights[right]:
            right -= 1
        else:
            left += 1
            right -= 1
    return largest
        
