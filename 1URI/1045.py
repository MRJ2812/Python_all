get = [float(x) for x in input().split()]

get.sort(reverse=True)

A, B, C = get

if A >= B + C:
    print("NAO FORMA TRIANGULO")
elif A*A == B*B + C*C:
    print("TRIANGULO RETANGULO")
elif A*A > B*B + C*C:
    print("TRIANGULO OBTUSANGULO")
elif A*A < B*B + C*C:
    print("TRIANGULO ACUTANGULO")
if A == B == C:
    print("TRIANGULO EQUILATERO")
elif A == B != C or A != B == C or A == C != B:
    print("TRIANGULO ISOSCELES")







