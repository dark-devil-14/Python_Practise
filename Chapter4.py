# ------------------------------------------------------------------------
                                   #CONDITIONALS (IF/ELSE/ELIF)
# ------------------------------------------------------------------------

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

# ------------------------------------------------------------------------
#  The if statement evaluates a condition (an expression that results in True or False).
#  If the condition is true, the code block inside the if statement is executed.
#  If the condition is false, the code block is skipped.

a= int(input("Enter the age: ")) 

if(a>=18): #if TRUE then this condition gets executed
    print("Your are above age of conent")
    print("Good age")
elif(a<=0):
    print("Please enter a valid age")
else:
    print("Sorry Below the age of concent")

# Using variable in Conditionals
is_this_true = False
if is_this_true:
    print("Heyy!! this works , variables in if")
else:
    print("heey this is for false statmeent")


# ------------------------------------------------------------------------
                                    #LOGICAL OPERATORS
# ------------------------------------------------------------------------

# and - Returns True if both statements are true
# or - Returns True if one of the statements is true
# not - Reverses the result, returns False if the result is true

c = False
d = True

if (c and d):
    print("Heyy!! this is an example of AND operatoe( if both are true)")
elif(c or d):
    print("Hey this is an example of the or opretor if any one condition is TRUE")
elif(not c==d):
    print("Heyy this is an example of the not logical operator")
else:
    print("Opps none of them is true")



# ------------------------------------------------------------------------
                                    #Practise Problems
# ------------------------------------------------------------------------

#Problem Statement 1: write a program to find the greatest of all 4 numbers 
a1 = int(input("Enter number 1:  "))
a2 = int(input("Enter number 2:  "))
a3 = int(input("Enter number 3:  "))
a4 = int(input("Enter number 4:  "))

if(a1>a2 and a1>a3 and a1>a4):
    print("Greatest number is a1: ", a1)
if(a2>a1 and a2>a3 and a2>a4):
    print("Greatest number is a2: ", a2)
if(a3>a1 and a3>a2 and a3>a4):
    print("Greatest number is a3: ", a3)
if(a4>a1 and a4>a3 and a4>a2):
    print("Greatest number is a4: ", a4)


# Problem Statement 2:
'''
write a program to find that the student passed the exam  total 40% and 33% in
each subject to pass, asuume 3 subjects
'''

marks1 = int(input("Enter the marks 1 :  "))
marks2 = int(input("Enter the marks 2 :  "))
marks3 = int(input("Enter the marks 3 :  "))

total_marks = ((marks1 + marks2 + marks3)/300)*100

if (((marks1/100)*100 > 33) and ((marks2/100)*100 > 33) and ((marks3/100)*100 > 33) and  total_marks > 40):
    print("Horeey, congratulations you have passed this class total percentage ", round(total_marks,2),"%")
else:
    print("Failed, total percentage ", round(total_marks,2),"%")

#Problem Statement 3: (use of IN function)
"""
A spam comment is defined as a text containing follow keywords: 
"Make a lot of money", "Buy Now", "Subscribe this", "Click this", 
write a program to detech these SPAMS 
"""

p1 = "Make a lot of money"
p2 = "Buy Now"
p3 = "Subscribe this"
p4 = "Click this"

Enter_message = input("Enter your comment : ")

if((p1.lower() in Enter_message.lower()) or (p2.lower() in Enter_message.lower()) or (p3.lower() in Enter_message.lower()) or (p4.lower() in Enter_message.lower())):
    print("This comment is a spam")
else:
    print("This comment is not a spam")

#Problem Statement 4: write a program to check weather a username contain 10 characters or not 

user_id = input("Enter yout user name : ")

if(len(user_id)<= 10):
    print("Your user name contian less than 10 user characters ")
else:
    print("Hello Mr.", user_id)

#Problem Statement 4: write a program for grading system
da_101 = int(input("Enter marks for DA 101 : "))
da_102 = int(input("Enter marks for DA 102 : "))
da_103 = int(input("Enter marks for DA 103 : "))
da_104 = int(input("Enter marks for DA 104 : "))

total_marks  = ((da_101 + da_102 + da_103 + da_104)/400)*100

if(total_marks > 90 and da_101 > 35 and da_102 > 35 and da_103>35 and da_104> 35) :
    print("Grade: A (Excelent)")
elif((total_marks > 80 and total_marks<90 and da_101 > 35 and da_102 > 35 and da_103>35 and da_104> 35)):
    print("Grade: AB")
elif((total_marks > 70 and total_marks<80 and da_101 > 35 and da_102 > 35 and da_103>35 and da_104> 35)):
    print("Grade: BB")
elif((total_marks > 60 and total_marks<70 and da_101 > 35 and da_102 > 35 and da_103>35 and da_104> 35)):
    print("Grade: BC")
elif((total_marks > 50 and total_marks<60 and da_101 > 35 and da_102 > 35 and da_103>35 and da_104> 35)):
    print("Grade: CC")
elif((total_marks > 40 and total_marks<50 and da_101 > 35 and da_102 > 35 and da_103>35 and da_104> 35)):
    print("Grade: DD")
else:
    print("Grade: F")

