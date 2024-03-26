from sympy import *

r = lambda f, num: float(f.replace(x, num))
space = lambda *args: list(map(lambda x: str(round(x, 3)).ljust(9) if type(x) in (float, int) else str(x).ljust(9), args))

x = Symbol('x')
f = eval(input('f(x)=').replace('^', '**'))
g = f.diff(x)
e, temp = 1, 5
print(*space('x', 'f(x)', 'f\'(x)', 'E'))

while e > 0.01:
    if 0 not in (r(f, temp), r(g, temp)):
        value = round(temp - r(f, temp)/r(g, temp), 3)
        e = abs(temp - value)
        print(*space(temp, r(f, temp), r(g, temp), e))
        temp = value
    else:
        temp += 0.01

print(*space(temp, r(f, temp), r(g, temp), 0))
