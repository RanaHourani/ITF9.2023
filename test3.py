#def add(x,y):
   # total=x+y
    #print(total)
#add(x=10,y=20)

#def sub(x,y):
#sub(x=10,y=20)
#def div(x,y):
   # total=x/y
   # print(total)
#div(x=10,y=20)
#def mul(x,y):
  #  total=x*y
   # print(total)
#mul(x=10,y=20)

#total=0
#for i in range(0,101):
   # total+=i
#print(total)

#for i in range(0,12):
  # print(f'6 * {i}= {i*6}')

#sum=0
#a=int(input("enter the nummber 1"))
#b=int(input("enter the nummber 2"))
#sum= a+b
#print(sum)

#sub=0
#a=int(input("enter the nummber 1"))
#b=int(input("enter the nummber 2"))
#sub=a-b
#print(sub)

length=int(input("enter the nummber 1"))
breadth=int(input("enter the nummber 1"))
area=length*breadth
print(area)

a=int(input("enter the length of 1 side"))
b=int(input("enter the length of 2 side"))
c=int(input("enter the length of 3 side"))

p= (a+b+c)
s=p/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("the area of tringle is %.2f"%area)

r=int(input("enter the radius:"))
area=3.14*r*r
print("the area is:",area)