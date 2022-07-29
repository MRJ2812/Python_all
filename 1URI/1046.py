x,y = [int(x) for x in input().split()]

    
if x == y:
        print(f"O JOGO DUROU 24 HORA(S)")
else:
    if x<y:
      print(f"O JOGO DUROU {abs(y-x)} HORA(S)")
    else:
      print(f"O JOGO DUROU {(24-x)+y} HORA(S)")