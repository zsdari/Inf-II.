def osszead (num1, num2):
    return num1 + num2

def axb (a, b):
    if a == 0:
        return None
    else:
        return -b / a

import math

def ax2b(a, b, c):
    if a == 0:
        if b == 0:
            return None
        else:
            x = -c / b
            return x, x

    determinant = b ** 2 - 4 * a * c

    if determinant < 0:
        return None
    else:
        sqrt_det = math.sqrt(determinant)
        x1 = (-b + sqrt_det) / (2 * a)
        x2 = (-b - sqrt_det) / (2 * a)
        return x1, x2

if __name__ == "__main__":
    print(osszead(10, 20))