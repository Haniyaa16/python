import os
files=os.listdir()
print("Ascending : ",sorted(files))
print("Descending : ",sorted(files,reverse=True))
