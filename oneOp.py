def test(nums: list[int], k: int) -> int:
    count = 0
    left = 0
    nums = [n for n in nums if n < k]
    nums = sorted(nums)
    right = len(nums) - 1

    while left < right:
        if nums[left] + nums[right] == k:
            count += 1
            nums.pop(right)
            nums.pop(left)
        elif nums[left] + nums[right] > k:
            nums.pop(right)
        else:
            nums.pop(left)
        
        right = len(nums) - 1

    return count

nums = [4,8,3,5,2,9,7,6,2,8,1]
k = 12
test(nums, k)
