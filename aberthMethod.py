import math
import random

def     getUpperLowerBounds(f):
    degree = f.degree
    coef = f.coef
    upper = 1 + 1 / abs(coef[-1]) * max(abs(coef[x]) for x in range(degree))
    lower = abs(coef[0]) / (abs(coef[0]) + max(abs(coef[x]) for x in range(1, degree + 1)))
    return upper, lower

def     initRoots(f):
    degree = f.degree
    upper, lower = getUpperLowerBounds(f)

    roots = []
    for i in range(degree):
        radius = random.uniform(lower, upper)
        angle = random.uniform(0, math.pi*2)
        root = complex(radius * math.cos(angle), radius * math.sin(angle))
        roots.append(root)

    return roots

def     aberthMethod(f):
    roots = initRoots(f)
    iteration = 0
    
    while True:
        valid = 0
        for k, r in enumerate(roots):
            ratio =  f.image(r) / f.derivative(r)
            offset = ratio / (1 - (ratio * sum(1/(r - x) for j, x in enumerate(roots) if j != k)))
            if round(offset.real, 12) == 0 and round(offset.imag, 12) == 0:
                valid += 1
            roots[k] -= offset
        if valid == len(roots):
            break
        iteration += 1

    return iteration, roots
