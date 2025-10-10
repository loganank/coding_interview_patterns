def triplet_sum(nums: List[int]) -> List[List[int]]:
    # sort list so you don't get dupes in set
    sorted_nums = sorted(nums)
    triplets = set()
    for i in range(len(sorted_nums)):
        find_pairs = sum_two_pointer_sorted(sorted_nums, i + 1, -nums[i])
        for pair in find_pairs:
            triplets.add(pair)
    return [list(triplet) for triplet in triplets]
    
def sum_two_pointer_sorted(nums, start, target):
    left = start
    right = len(nums) - 1
    pairs = set()
    while left < right:
        print(left)
        print(right)
        currentSum = nums[left] + nums[right]
        if currentSum == target:
            pairs.add((-target, nums[left], nums[right]))
            left += 1
        elif currentSum < target:
            left += 1
        else: 
            right += -1
    return pairs
