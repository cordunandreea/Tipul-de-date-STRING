n=str(input('primul cuvant este:'))
a=str(input('al doilea cuvant este:'))
b=str(input('al treilea cuvant este:'))
c=str(input('al patrulea cuvant este:'))
x=str(n)
y=str(a)
z=str(b)
q=str(c)
e=0
if len(x)>=3 and len(y)>=3 and len(z)>=3:
    e=(len(z))/2
    i=int(e)
    l=x[:2]
    m=y[0]
    o=z[:3]
    p=q[:i]
    print(n,a,b,c,sep=' ')
    print(str(l)+str(m)+str(o)+str(p))
else:
    print('eroare, nu corespunde conditiei')