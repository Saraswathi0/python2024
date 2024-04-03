name = input("")  # taking the input as string
l1 = ['a', 'e', 'i', 'o', 'u']
len = len(name)
name = name.lower()
v = 0
c = 0  # initialize the vowels and consonants counts

def count_vowels_and_consonants(name,v,c):
    global v, c                                     #function defintion
    for i in range(len):
        if name[i] in l1:
            v += 1
        else:
            c += 1
    r = {"vowels": v, "consonants": c}
    return r

print(count_vowels_and_consonants(name,0,0))  #function calling 
