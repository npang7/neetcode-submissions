class Solution:
    def myPow(self, x, n):
        def helper(x, n):
            if x == 0:
                return 0

            if n == 0:
                return 1

            # 底数平方，指数减半
            next_x = x * x
            next_n = n // 2
            res = helper(next_x, next_n)

            # 奇数指数需要额外乘一个当前层的 x
            if n % 2 == 1:
                return x * res
            else:
                return res

        res = helper(x, abs(n))

        if n < 0:
            return 1 / res
        else:
            return res