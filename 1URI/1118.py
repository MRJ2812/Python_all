sum = 0
i = 0
lst = []
while True:
    
    get = float(input())
    if 0<= get <= 10:
       sum += get
       i += 1 
    else:
        lst.append("nota invalida")
        
    if i == 2:
        avg = sum / 2
        lst.append(f"media = {avg}")
        sum = 0
        
        
        
        a = True
        while a:
            lst.append("novo calculo (1-sim 2-nao)")
            get2 = int(input())
            if 1 <= get2 <= 2:
                if get2 == 1:
                    i = 0
                    break
                else:
                    a =False
        else:
            break
  
            
[print(x) for x in lst]
