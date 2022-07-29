a,b,c = [float(x) for x in input().split()]



if a+b>c and a+c>b and b+c>a:
    print("Perimetro =",a+b+c)
else:
    print("Area =",(a+b)*c/2)