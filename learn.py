#First Python Programming 
#Credits : Prof Dr Neeraj Kumar Sharma   (IITG)

#----------------------------------------------------------------------------------------------------------------
#Variables ( Containers which store values )
name = 'Jhon'
age = 35
total_cost = 32.12
is_valid = True
print(f"\nUser: {name}   |   Age: {age}   |   Cost: {total_cost}   |   Valid: {is_valid}")
print(type(name), type(age), type(total_cost), type(is_valid))

x = "\nRajuram "
y = "Bsc Student " 
z = "2029"
print(x+y+z)

#----------------------------------------------------------------------------------------------------------------
#Operating on Variables [parrentheses, exponential, division, multiplication, addition, subtraction] -- LEFT -> RIGHT -- 
a = 2 * ( 3 + 4 ) ** 2
print(a)

#Logical operator
a = True
b = False

c = a and b #AND Operator
d = a or b #OR Operator
print(c, d)

#Area of the rectangle 
length = float(input("Length of the rectangle: "))
breadth = float(input("Breadth of the rectangle: "))

Area = length * breadth #result 

print(f"The area of the rectangle the is : {Area} sq.cm")
