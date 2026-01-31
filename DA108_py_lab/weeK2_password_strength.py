
# Password Strength Checker with Feedback Loop
# Implement a password strength checker that evaluates a given password while reinforcing the
# understanding of fundamental data types like int, float, bool, string, and list. The program should
# provide real-time feedback and allow users to retry until they create a strong password.
criteria = 0.0

def validation_of_password(password):
    length = len(password) #check length of the password
    check_is_upper = any(char.isupper() for char in password) #check is there anything in upper case in pass
    check_is_lower = any(char.islower() for char in password) #check is there anything in lower case in pass
    check_is_num   = any (char.isnumeric() for char in password) #check is there anything in numeric in pass
    check_special_char = "@#$!*&%?"
    check_special_char_ = any(char in check_special_char for char in password)
    condition_verification = [check_is_upper, check_is_lower , check_is_num, check_special_char_ , length > 8 ]
    criteria = (sum(condition_verification)/5)*100

    if(criteria < 30.0 ):
        print("Weak Pasword, Try using numbers and special characters.")
        return False
    elif(criteria < 80.0):
        print("Medium Passwrd, Try adding a special character for a stronger password.")
        return False
    else:
        print("Strong password! Great job!")
        return True



#Login Page
usr_name = input("Please Enter Your Username : ")
while(1):
    usr_pass = input("Please Enter Your Password : ")
    sucess = validation_of_password(usr_pass)
    if sucess:
        print("Congratlation Account created sucessfull")
        break


