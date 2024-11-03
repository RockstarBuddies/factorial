from cmath import sin, sqrt, pi, exp


g = 7
n = 9
p = [0.99999999999980993,676.5203681218851,-1259.1392167224028,771.32342877765313,-176.61502916214059,12.507343278686905,-0.13857109526572012,9.9843695780195716e-6,1.5056327351493116e-7]

EPSILON = 1e-07
def drop_imag(z):
    if abs(z.imag) <= EPSILON:
        z = z.real
    return z

def gamma(z):
    z = complex(z)
    if z.real < 0.5:
        y = pi / (sin(pi * z) * gamma(1 - z))
    else:
        z -= 1
        x = p[0]
        for i in range(1, len(p)):
            x += p[i] / (z + i)
        t = z + g + 0.5
        y = sqrt(2 * pi) * t ** (z + 0.5) * exp(-t) * x
    return drop_imag(y)

inp=eval(input("Enter element "))
if inp==0:
    print("1")
else:
    print(gamma(inp+1))
