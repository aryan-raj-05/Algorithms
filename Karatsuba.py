class Karatsuba:
    @staticmethod
    def multiply(x: str, y: str):
        x, y, n = Karatsuba._make_equal_len(x, y)

        if n == 1:
            return int(x) * int(y)
            
        a, b = Karatsuba._split(x)
        c, d = Karatsuba._split(y)

        full = Karatsuba.multiply(a, c)
        ones = Karatsuba.multiply(b, d)
        half_a = Karatsuba.multiply(a, d)
        half_b = Karatsuba.multiply(b, c)

        n = n + 1 if n % 2 != 0 else n
        return ((10 ** n) * full) + (ones) + ((10 ** (n // 2)) * (half_a + half_b))
        
    @staticmethod
    def _split(nums: str):
        if len(nums) != 1:
            return nums[0: len(nums) // 2], nums[len(nums) // 2:]
        
    @staticmethod
    def _make_equal_len(a: str, b: str):
        if len(a) < len(b):
            for _ in range(len(b) - len(a)):
                a = '0' + a
        elif len(b) < len(a):
            for _ in range(len(a) - len(b)):
                b = '0' + b
        return a, b, len(a)
        