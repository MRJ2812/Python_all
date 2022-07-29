get = float(input())

if get >= 0 and get <= 25:
   print('Intervalo [0,25]')
   
elif get > 25.0 and get <= 50.0:
   print('Intervalo (25,50]')
   
elif get > 50 and get <= 75:
   print('Intervalo (50,75]')
   
elif get > 75 and get <= 100:
   print('Intervalo (75,100]')
     
else:
  print('Fora de intervalo')