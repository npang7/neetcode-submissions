class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1

        res = 1
        power = abs(n)

        while power > 0:
            # 指数是奇数，先把多出来的一个 x 乘进答案
            if power % 2 == 1:
                res = res * x

            # 底数平方，剩余指数减半
            x = x * x
            power = power // 2 #power最终变成0，当1 // 2时

        if n < 0:
            return 1 / res
        else:
            return res