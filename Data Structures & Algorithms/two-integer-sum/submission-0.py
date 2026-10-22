class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_nums = {}
        sum_nums = []
        for i, num in enumerate(nums):
            target_num = target - num
            if target_num in seen_nums:
                sum_nums.append(seen_nums[target_num])
                sum_nums.append(i)
                return sum_nums
            seen_nums[num] = i

