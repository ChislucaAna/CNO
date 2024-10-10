from domain import Complex
import math

class QuadraticSolver:
    def solve_quadratic(self, a, b, c):

        if isinstance(a, Complex) and a.real == 0 and a.imaginar == 0:
            raise ValueError("a trebuie sa fie pozitiv pentru a aplica algoritmul de rezolvare.")

        delta = (b * b) - (4 * a * c)

        if delta.real > 0 and delta.imaginar == 0: ##cazul clasic
            root1 = (math.sqrt(delta.real) - b) / (2 * a)
            root2 = ((-1) * (b + math.sqrt(delta.real))) / (2 * a)
        else:
            real_part = -b.real / (2 * a.real) #partea dinainte de radical e reala
            imag_part = math.sqrt(-delta.real) / (2 * a.real) #partea cu radicalul e coeficientul lui i
            root1 = Complex(real_part, imag_part)
            root2 = Complex(real_part, -imag_part)

        return root1, root2
