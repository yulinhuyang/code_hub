class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        f = [1] * (n)

        for i in range(n):
            for j in range(i):
                if nums[j]  < nums[i]:
                    f[i] = max(f[i], f[j] + 1)
        
        res = 0
        for i in range(n):
            res = max(res, f[i])
        return res
        
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        stack = []

        def find_index(num):
            l, r = 0, len(stack)
            while l < r:
                mid = l + r >> 1
                if stack[mid] >= num:
                    r = mid 
                else:
                    l = mid + 1

            return r


        for num in nums:
            if not stack or num > stack[-1]:
                stack.append(num)
            else:
                position = find_index(num)
                stack[position] = num

        return len(stack)
