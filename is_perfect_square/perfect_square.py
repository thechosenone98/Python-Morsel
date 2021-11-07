from decimal import Decimal
import decimal

class ComplexDecimal(object):
    def __init__(self, value) -> None:
        super().__init__()
        self.real = Decimal(value.real)
        self.imag = Decimal(value.imag)
    
    def __str__(self):
        sep = '+' if self.imag >= 0 else ''
        return f'({str(self.real)}{sep}{str(self.imag)}j)'

    def __add__(self, other):
        result = ComplexDecimal(self)
        result.real += other.real
        result.imag += other.imag
        return result

    def __truediv__(self, other):
        result = ComplexDecimal(self)
        if isinstance(other, (int, float, Decimal)):
            result.real /= other.real
            result.imag /= other.real
        elif isinstance(other, ComplexDecimal):
            denom = other.real ** 2 + other.imag ** 2
            result.real = ((self.real * other.real) + (self.imag + other.imag)) / denom
            result.imag = ((self.imag * other.real) - (self.real * other.imag)) / denom
        return result

    def complex_mul(a, b):
        result = ComplexDecimal(0)
        result.real = a.real * b.real - a.imag * b.imag
        result.imag = a.real * b.imag + a.imag * b.real
        return result

    def __mul__(self, other):
        result = ComplexDecimal(self)
        if isinstance(other, (int, float, Decimal)):
            result.real *= other.real
            result.imag *= other.real
        elif isinstance(other, ComplexDecimal):
            result = ComplexDecimal.complex_mul(self, other)
        elif isinstance(other, complex):
            other = ComplexDecimal(other)
            result = ComplexDecimal.complex_mul(self, other)
        return result

    def __rmul__(self, other):
        return self.__mul__(other) 

    def norm(self):
        return (self.real ** 2 + self.imag ** 2).sqrt()

    def sqrt(self, secondary=False):
        """Return both complex square root of the ComplexDecimal number"""
        if self.imag:
            r = self.norm()
            z_r = self + self.norm()
            result = r.sqrt() * (z_r / z_r.norm())
        elif self.real > 0:
            result = ComplexDecimal(self.real.sqrt())
        else:
            result = ComplexDecimal(0)
            result.imag = abs(self.real).sqrt()
        if secondary:
            result.real *= -1
            result.imag *= -1
        return result
        
        

def is_perfect_square(n, *, complex = False):
    with decimal.localcontext() as c:
        c.prec = 2000
        if complex:
            n_complex = ComplexDecimal(n)
            n_complex_sqrt = n_complex.sqrt()
            return False if (n_complex_sqrt.real % 1 != 0 or n_complex_sqrt.imag % 1 != 0) else True
        else:
            return False if n < 0 else Decimal(n).sqrt() % 1 == 0

if __name__ == "__main__":
    # print(is_perfect_square(25))
    # print(is_perfect_square(64))
    # print(is_perfect_square(4624000000000000))
    # print(is_perfect_square(4623999999999999))
    # print(is_perfect_square(-5))
    test = ComplexDecimal(512j)
    print(test.sqrt(secondary=False))
    print(ComplexDecimal(-4+3j) * 4)
    print((-4-3j) * ComplexDecimal(-4+3j))