class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nums = [element for innerList in matrix for element in innerList]

        left = 0
        right = len(nums)

        while left < right:
            mid  = (right+left) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                left += 1
            else:
                right -= 1
        return False


