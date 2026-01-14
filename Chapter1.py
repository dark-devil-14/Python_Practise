# # In python print to print multiple line you use """ : print(""" """)

# #Variable and TYPE_CASTING
# a = 43
# b = float(a)
# print(type(b))
# print(b)

# #Input
# #Problem statement 1 : python program to add two number
# a = int(input("enter the numnber 1: "))
# b = int(input("enter the numnber 2: "))
# print(f"Number a is : {a}" )
# print(f"Number b is : {b}" )
# print("sum is ", a+b)


# #Problem statement 2 : Write a python program to print the type of the input 
# a = input("Enter :")
# print(type(a))

# #Problem statement 3 : Write a python program to find a is greater than b or not 
# a = float(input("enter the number a: "))
# b = float(input("enter the number b: "))
# if(a>b) :
#     print("a is greater than b ")
# elif(a<b):
#     print("b is greater than a ")
# else:
#     print("Both are equal")


# #Problem statement 4 :(basic) Write a python program to find the average of the number
# a = float(input("Enter the number 1: "))
# b = float(input("Enter the number 2: "))
# print("Average of these two number is " ,(a+b)/2)

#Problem statement 5 :(basic) Write a python program to find the square of the number
# a = float(input("Enter Your number : "))
# print("the sqaure of the number is : ", a**2)

# # --------------------------------------------------------------------------------------------
# # STRING (DATA TYPE IN PYHTON , STRING IS A SEQUENCE OF CHARACTERS)
# # STRING IS IMMUTABLE (YOU CANT CHANGE THE EXISTING STRING)
# #Escape sequence character : \n, \t, \b, \\
# name = "harry"
# nameshort = name[1:3] #start from index 0 all the way till 3(excluding)
# print(nameshort)
# print(len(name))
# print(name.startswith("h"))
# print(name.upper())
# print(name.capitalize())

# # ----Practise-----
# # Problem statement 1: write a python program to display a user entered name followed by good after noom using input() function 
# user_name = input("Enter you name: ")
# print(f"Heyy Good afternoon {user_name}!!\nGlad to see you again")

# #Problem statemenT 2 :  REPLACE 
# offer_leter  = '''Dear <name>, 
# Congratulations, You are selected!!
# Joining Date: <Date> '''
# print(offer_leter.replace("<name>","Rajuram D").replace("<Date>","February 24 2025"))

# #Problem statement 3 : Finding double space position in a variable
# # print(name.find("  "))

