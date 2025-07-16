class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        n=x
        s = 0
        for d in str(x):
            s = s + int(d)
        if n % s == 0:
            return s
        else:
            return -1
