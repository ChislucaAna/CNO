import math

class Complex:
    def __init__(self, real=0, imaginar=0):
        self.real = real
        self.imaginar = imaginar

    def __add__(self, other):
        sumareal = self.real + other.real
        sumaimaginar = self.imaginar + other.imaginar
        return Complex(sumareal, sumaimaginar)
       
    def __sub__(self, other):
        diffreal = self.real - other.real
        diffimaginar = self.imaginar - other.imaginar
        return Complex(diffreal, diffimaginar)

    def __mul__(self, other):
        mulreal = self.real * other.real - self.imaginar * other.imaginar
        mulimaginar = self.real * other.imaginar + self.imaginar * other.real
        return Complex(mulreal, mulimaginar)

    def __truediv__(self, other):
        numitor = other.real ** 2 + other.imaginar ** 2
        if numitor != 0:
            divreal = (self.real * other.real + self.imaginar * other.imaginar) / numitor
            divimaginar = (self.imaginar * other.real - self.real * other.imaginar) / numitor
            return Complex(divreal, divimaginar)
        else:
            raise ZeroDivisionError("Cannot divide by zero complex number")

    def __str__(self):
        return f"{self.real} + {self.imaginar}i"

    def __eq__(self, other):
        return self.real == other.real and self.imaginar == other.imaginar

    def __abs__(self):
        return math.sqrt(self.real ** 2 + self.imaginar ** 2)


