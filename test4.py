
def get_sum(num1,num2):
    return num1+num2
def get_sub(num1,num2):
    return num1-num2
def get_mul(num1,num2):
    return num1*num2
def get_div(num1,num2):
    return num1/num2

def get_inputs():
    num1=int(input("enter nummber1:"))
    num2=int(input("enter nummber2:"))
    return [num1,num2]
while True:
    selection = int(input("""1. sum
    2. Subtract
    3. Multiply
    4. Division
    5. Calculate triangle area
    6. Calculate circle area
    7. Calculate rectangle area
    8. Exit"""))

if selection == 8:
      exit()
elif selection == 1:
     nummbers=get_inputs()
     result=get_sum(nummbers[0],nummbers[1])
     print(f"sum{nummbers}=",result)
elif selection == 2:
     nummbers=get_inputs()
     result=get_sub(nummbers[0],nummbers[1])
     print(f"sub{nummbers}=",result)
elif selection == 3:
    nummbers=get_inputs()
    result=get_mul(nummbers[0],nummbers[1])
    print(f"mul{nummbers}=",result)
elif selection == 4:
    nummbers=get_inputs()
    result=get_div(nummbers[0],nummbers[1])
    print(f"div{nummbers}=",result)
elif selection == 5:
    length=int(input("enter nummber1"))
    breadth=int(input("enter nummber2"))
    area=length*breadth
    print(area)
elif selection == 6:
    r=float(input("enter radius of circle:"))
    area=3.14156*r*r
    print("area of circle is",area)
elif selection == 7:
    a=float(input("enter value of base:"))
    b=float(input("enter value of hight:"))
    area=0.5*a*b
    print("\n area of triangle is:",area)



