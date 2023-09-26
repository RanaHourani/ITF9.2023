

d1= {"Name" : "Ahmed" , "Age" : 23}
d2 = {"City" : "Gaza", "Gender" : "Male"}
d3 = {}
for d in (d1, d2): d3.update(d)
print(d3)
Concatenate_Dicts = {'Name' : 'Ram', 'Age' : 23, 'City' : 'Salem', 'Gender': 'Male'}

while True:
 try:
    ength=int(input("enter nummber1"))
    breadth=int(input("enter nummber2"))
    area=length*breadth

    if area < 0 :
        print("invalid input , area must be bigger than zero ")
    else:
        break
 except:
     print("invalid input")

area=length*breadth
print(area)
