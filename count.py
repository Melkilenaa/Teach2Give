# Write a program that counts the number of vowels in a sentence.
Str=input("enter a sentence:")
vow=0
vowels='a,e,i,o,u'
record=[]
# Use append opeartion to rule out repetitive vowels.
for i in Str:
    if i in vowels and i not in record:
        record.append(i)
        vow+=1
print(vow)