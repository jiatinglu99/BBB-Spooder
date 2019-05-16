import math

class DegreeMath:
    @staticmethod
    def sin(a):
        return math.sin(math.radians(a))

    @staticmethod
    def cos(a):
        return math.cos(math.radians(a))

    @staticmethod
    def tan(a):
        return math.tan(math.radians(a))

    @staticmethod
    def asin(x):
        return math.degrees(math.asin(x))

    @staticmethod
    def acos(x):
        return math.degrees(math.acos(x))

    @staticmethod
    def atan(x):
        return math.degrees(math.atan(x))

    @staticmethod
    def atan2(y, x):
        return math.degrees(math.atan2(y, x))

    @staticmethod
    def sqrt(x):
        return math.sqrt(x)
        
    @staticmethod
    def sqrd(x):
        return math.pow(x, 2)
