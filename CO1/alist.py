names=["Anu","Amal","Vinu","jessia","rossia"]
count = 0
for name in names:
  count +=name.lower().count("a")
print("Names = ",names)
print("Count of 'a' =",count)
