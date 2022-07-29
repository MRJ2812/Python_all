# This will help us too set password

import re
str = r"[joy]"                            

if re.search(str,"JOY"):                # We can take input this value
    print("Match")
else:
    print("Not match")
    
    
    
#---------------------------------------------

num = r"[0-9][A-Z][a-z]"            # Must a num,, capital letter,, small letter

if re.search(num, "0Ag"):
    print("Match")
else:
    print("Not match")
    
    
## Now go to "Regular Expression_class"