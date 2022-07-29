a = [float(x) for x in input().split()] 
 
Media = sum(a) / len(a)

print("Media: %.1f" % Media) 


if Media >= 7.0:
    print("Aluno aprovado.")
    
if Media < 5.0:
    print("Aluno reprovado.")
    
if 5.0 <= Media <=6.9:
    print("Aluno em exame.")
    
    score = float(input())
    print(f"Nota do exame: {score}")
    
    sum2 = (Media+score) / 2
    if sum2 >= 5.0:
        print("Aluno aprovado.")
    if sum2 <5.0:
        print("Aluno reprovado.")
    sum3 = (Media+score)/2
    print("Media final: %.1f" %sum3)
    
