# x,y -- hr ,, m,n -- minute
x,m,y,n = [int(x) for x in input().split()]

    
if x == y and m == n:
        print(f"O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else:
    if x<y and m<n:
        print(f"O JOGO DUROU {abs(y-x)} HORA(S) E {abs(n-m)} MINUTO(S)")
    elif x<y and m>n:
        print(f"O JOGO DUROU {(abs(y-x))-1} HORA(S) E {(60-m)+n} MINUTO(S)")
    elif x>y and m<n:
        print(f"O JOGO DUROU {(24-x)+y} HORA(S) E {abs(n-m)} MINUTO(S)")
    elif x>y and m>n:
        print(f"O JOGO DUROU {((24-x)+y)-1} HORA(S) E {(60-m)+n} MINUTO(S)")