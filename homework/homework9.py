word=input("Enter a word:")
d=dict()
for a in word:
    if a in d:
        d[a]+=1
    else:
        d[a]=1
print(d)