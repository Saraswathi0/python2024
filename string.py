name=input("")
l1=['a','e','i','o','u']
len=len(name)
name=name.lower()
v=0
c=0
for i in range(len):
    if name[i]in l1:
        v=v+1
    else:
        c=c+1
r={"vowels":v,"constant":c}
print(r)
