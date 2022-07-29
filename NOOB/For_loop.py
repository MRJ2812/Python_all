# After loop stop print else

for x in range(6):
  print(x)
else:
  print("Finally finished!")
  
  
# If loop break else condition not exicute

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")