text=(input("Enter the text : "))
words = text.split()
for word in words:
    print(word,"-",words.count(word))
