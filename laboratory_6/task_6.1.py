class Complex():
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Complex(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Complex(self.x - other.x, self.y - other.y)
    def __truediv__(self, other):
        return Complex(self.x / other.x, self.y / other.y)
    def __mul__(self, other):
        return Complex(self.x * other.x, self.y * other.y)
    def __abs__(self):
        return Complex((self.x**2+self.y**2)**(1/2) , 0)
    def __str__(self):
        if self.x >= 0:
            xstr = '{}'.format(self.x)
        else:
            xstr = '{}'.format(self.x)
        if self.y >= 0:
            ystr='+{}j'.format(self.y)
        else:
            ystr = '{}j'.format(self.y)
        pr='({}{})'.format(xstr,ystr)
        return pr

a=Complex(-2,1)
b=Complex(3,0)
print(a)
print(abs(b-a))