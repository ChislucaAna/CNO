import math

class Complex:
    def __init__(self, real=0, imaginar=0):
        if isinstance(real, str):
            self.real, self.imaginar = self.from_string(real)
        else:
            self.real = real
            self.imaginar = imaginar
    
    @staticmethod
    def from_string(s): #metodele statice nu au referinta self si nu lucreaza cu obiecte din acea clasa
        #scoatem spatiile extra din string pt parsare mai usoara
        s = s.replace(" ", "").rstrip('i')
        #gaseste minus sau plus
        last_plus = s.rfind('+')
        last_minus = s.rfind('-')
        #determina pozitia de split
        split_pos = max(last_plus, last_minus)
        #totul inainte de pozitia de split e partea reala, totul dupa e imaginar
        real_part = s[:split_pos]
        imag_part = s[split_pos:]
        #converteste in int cele doua parti pt a creea instanta
        return int(real_part), int(imag_part)

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


