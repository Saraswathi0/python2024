name=input("")                   #taking the input as string
l1=['a','e','i','o','u']
len=len(name)
name=name.lower()
v=0
c=0                  #initialize the vowels and  consonants counts
for i in range(len):
    if name[i]in l1:
        v=v+1
    else:
        c=c+1
r={"vowels":v," consonants ":c}    
print(r)
