count = int(input())

c = 0
r = 0
s = 0
total_num = 0
x = ''
num = 0
for i in range(0,count):
    
    x,name = input().split()
    
    num = int(x)
    total_num += num
    if name == 'C':
        c += num
    elif name == 'R':
        r += num
    elif name == 'S':
        s += num
    
print(f"Total: {total_num} cobaias ")
print(f"Total de coelhos: {c}")  
print(f"Total de ratos: {r}")  
print(f"Total de sapos: {s}")  

print(f"Percentual de coelhos: {100*(c/total_num):0.2f} %")
print(f"Percentual de ratos: {100*(r/total_num):0.2f} %")
print(f"Percentual de sapos: {100*(s/total_num):0.2f} %")

 