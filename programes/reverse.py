n= input ("enter any 5 digit no.")
m=int(n)
a=int(m%10)
print(a)
m=int(m/10)
b=int(m%10)
print(b)
m=int(m/10)
c=int(m%10)
print(c)
m=int(m/10)
d=int(m%10)
print(d)
m=int(m/10)
e=int(m)
print(e)
print(a*10000+b*1000+c*100+d*10+e)