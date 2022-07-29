sum = 0
i = 0
lst = []



while True:
    get = float(input())
    if 0<= get <= 10:
        sum += get
        i += 1
        if i == 2:
            avg = sum/2
            lst.append(f"media = {avg}")
            break
    else:
        lst.append("nota invalida")


for i in lst:
    print(i)