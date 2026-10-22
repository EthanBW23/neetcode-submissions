class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_nums = {}
        for i, num in enumerate(nums):
            target_num = target - num
            if target_num in seen_nums:
                return [seen_nums[target_num], i]
            seen_nums[num] = i

