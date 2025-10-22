class Solution:
    def findMedianSortedArrays(self, A, B):
        A, B = sorted((A, B), key=len)
        m, n = len(A), len(B)
        total = m + n
        half = total // 2

        l, r = 0, m - 1
        while True:
            i = (l + r) // 2  # A's partition
            j = half - i - 2  # B's partition

            Aleft = A[i] if i >= 0 else float('-inf')
            Aright = A[i + 1] if i + 1 < m else float('inf')
            Bleft = B[j] if j >= 0 else float('-inf')
            Bright = B[j + 1] if j + 1 < n else float('inf')

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1

