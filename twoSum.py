class Solution(object):
    def twoSum(self, nums, target):
        index = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target:
                    if j != i and i not in index and j not in index:
                        index.append(i)
                        index.append(j)
        return index