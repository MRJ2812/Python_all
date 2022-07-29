import re

str = r"Joy"

if re.search(str,"Hi my name is Joy"):
    print("Yes")
else:
    print("No")
    
    
# -------------------- substitute ----------------------

pattern = r"Joy"

txt1 = "hi my name is Joy"

text2 = re.sub(pattern, "Noone", txt1)

print(text2) 

