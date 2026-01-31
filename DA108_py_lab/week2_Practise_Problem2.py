# Write a python program (script) which asks for user input by showing the prompt user input. It reads
# the input, does some processing and outputs the message received as input but with the case altered.


#Take user input 
while(1):
    usr_input = input("Enter the user input: ")
    new_usr_input =""

    for i in usr_input:
        if(i.isupper()):
            new_usr_input += i.lower()
        elif(i.islower()):
            new_usr_input += i.upper()
        else:
            new_usr_input += i
    print(new_usr_input)
# RAJUram -- > rajuRAM
