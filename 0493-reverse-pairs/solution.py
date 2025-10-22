class Solution:
    def reversePairs(self, nums):
        def merge_sort(arr):
            if len(arr) <= 1: return 0, arr
            mid = len(arr)//2
            left_count, L = merge_sort(arr[:mid])
            right_count, R = merge_sort(arr[mid:])
            count = left_count + right_count
            j = 0
            for i in range(len(L)):
                while j < len(R) and L[i] > 2 * R[j]:
                    j += 1
                count += j
            return count, sorted(L + R)
        return merge_sort(nums)[0]

