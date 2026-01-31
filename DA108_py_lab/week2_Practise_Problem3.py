# Often while listening to a lecture on youtube we slow down/speed up the playback speed. In this task
# you will do something similar but with text. The program should work as follows.
# $ python task_B.py

# user input: Hello! I am Tommy!
# output: Hello! ... I ... am ... Tommy!

#take input
usr_input = input("Enter your name: ")
new_string = " "
print(usr_input.isspace())

for x in  usr_input: 
    if x == " " :
        new_string +=  x + "......."
    else:
        new_string += x

print(new_string)
