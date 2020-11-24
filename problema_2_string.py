str=input('Dati un sir de caractere:')
lm=0
c=0
a=0
for i in str:
    lm+=i.isupper()
print('in sir se gasesc',lm,'litere majuscule')
for i in str:
    c+=i.isdecimal()
print('in sir se gasesc',c,'cifre')
for i in str:
    if i.isalnum():
        continue
    if i.isspace():
        continue
    else:
        a+=1
    print('in sir se gasesc',a,'caractere speciale')