#write a programm to calculate the age based on thier birthday year 
#the program should show the reaming days left for their next birthday 
#the program should itself fetch the system date and time 

from datetime import date, datetime

print('Age Calculator with Birthday Count \nWelcome, Please Enter your DOB in YYYY/MM/DD')
user_dob = input()
dob_converter = datetime.strptime(user_dob, '%Y-%m-%d').date()

#age calculation 
today_date = date.today()
print(f"Todays Date is : {today_date}")
user_age_difference = (today_date - dob_converter)//365
print(f"Your age is : {user_age_difference.days}")


#dob calculation 
dob_converter = datetime.strptime(user_dob, '%Y-%m-%d').date() #conver the string to date format
this_year_dob = dob_converter.replace(year = today_date.year) #convert your dob to present date of birth


if(today_date > this_year_dob): #if your dob is ahead of the current year birth date
    next_year_dob = dob_converter.replace(year = today_date.year + 1)
else:
    next_year_dob = this_year_dob

days_left_next_brdy =  (next_year_dob - today_date).days
print(f"Days left for upcoming birthday is : {days_left_next_brdy}")

print(today_date)
print(next_year_dob)


