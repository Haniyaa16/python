ls1=eval(input("Enter 1st list:"))
ls2=eval(input("Enter 2nd list:"))
if len(ls1) == len(ls2):
    print("Same Length")
else:
    print("Not having same length")
if sum(ls1) == sum(ls2):
     print("Having same sum")
else:
    print("Not having same sum")
common =[]
for x in ls1:
    if x in ls2 and x not in common:
        common.append(x)
print("Common values :",common)
    
