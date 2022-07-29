grenais = 0
inter_total = 0
Gremio_total = 0
draw = 0
lst = []
while True:
    inter,Gremio = [int(x) for x in input().split()]
    
    grenais += 1
    if inter > Gremio:
        inter_total += 1
    elif inter < Gremio:       
        Gremio_total += 1
    elif inter == Gremio:
        draw += 1
    
    # print("Novo grenal (1-sim 2-nao)")
    lst.append("Novo grenal (1-sim 2-nao)")
    get = int(input())
    if get == 1:
        continue
    else:
        lst.append(f"{grenais} grenais")
        lst.append(f"Inter:{inter}")
        lst.append(f"Gremio:{Gremio}")
        lst.append(f"Empates:{draw}")
        if inter_total >  Gremio_total:
            lst.append("Inter venceu mais")
        elif inter_total <  Gremio_total:
            lst.append("Gremio venceu mais")
        else:
            lst.append("Não houve vencedor")      
        break
    
[print(x) for x in lst]

