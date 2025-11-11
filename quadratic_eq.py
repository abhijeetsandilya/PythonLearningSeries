a=int(input("enter the value of a"))
b=int(input("enter the value of b "))
c=int(input("enter the value of c"))
d=(b**2-4*a*c)
if d<0:
       value1="imaginary"
       value2 = "imaginary"
elif d==0:
       value1=(-b+d**0.5)/2*a
       value2=(-b-d**0.5)/2*a
else:
        value1 = (-b+d**0.5)/2*a
        value2 = (-b-d**0.5)/2*a

print(value1,value2)

