a='Ank it saraswat'
a=a.lower()
vowel=0
consonants=0
space=0
for i in range(0,len(a)):
    if a[i] in ('a','e','i','o','u'):
        vowel+=1
    elif(a[i]>='a' and a[i]<='z'):
        consonants+=1
    elif(a[i]==' '):
        space+=1
print(vowel)
print(consonants)
print(space)
