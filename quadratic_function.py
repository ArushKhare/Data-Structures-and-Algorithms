import math

class Quadratic(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.discriminant = pow(b, 2) - (4 * a * c)

    def roots(self):
        sqrt = None
        if self.discriminant < 0:
            raise Exception('No roots were found')

        if self.discriminant == 0:
            return -self.b / (2 * self.a)

        if self.discriminant > 0:
            temp = math.sqrt(self.discriminant)
            if temp == int(temp):
                sqrt = temp
                sqrt /= 2 * self.a
                res1, res2 = None, None
                res1 = sqrt + (-self.b) / (2 * self.a)
                res2 = (-self.b) / (2 * self.a) - sqrt
                return tuple([res1, res2])

            else:
                sqrt = f'sqrt({self.discriminant})'
                res1 = f"(-{str(self.b)} + {sqrt}) / {2 * self.a}"
                res2 = f"(-{str(self.b)} - {sqrt}) / {2 * self.a}"
                return [res1, res2]

    def num_of_solutions(self):
        if self.discriminant < 0:
            return 0
        if self.discriminant == 0:
            return 1
        if self.discriminant > 0:
            return 2

    def y_intercept(self):
        return self.c

    def function(self, x):
        return (self.a * pow(x, 2)) + (self.b * x) + self.c
    
    def format(self):
        return f'f(x) = ({self.a})x^2 + ({self.b})x + {self.c}'


q = Quadratic(1, 6, 4)

print("roots:", q.roots())
print("function:", q.format())
print("y intercept:", q.y_intercept())
print('f(0):', q.function(0))
