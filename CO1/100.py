num=input('Enter numbers : ').split()
list=[]
for n in num:
    if int(n)>100:
        list.append('over')
    else:
        list.append(int(n))
print(list)
            
