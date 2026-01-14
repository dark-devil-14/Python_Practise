# ------------------------------------------------------------------------
                                   #LIST []
# ------------------------------------------------------------------------

# list : is the container to store the set of values 
#In python strings are unmutable but you can change the list

friends = ["rajuram", "orange", 4, 32.001, False, "Askasha", "romeo"]
print(friends[0]) #list indexing
friends[0] = "melvin" #list Mutation 
print(friends[0:4]) #index
friends.append("Harry") #list can be appended 

#sorting, reversing and Inserting in the list 
l1 = [1,5,7,3,10] 
l1.sort() #sorting
print(l1) 

l2 = [23, 65, 12, 44]
l2.reverse() #reversing
print(l2) 

l3 = ["rabbit", "melvin", 32.53]
l3.insert(1, 999) #Inserting: insert(array_index, value_to_be_inserted)
print(l3)

l4 = ["rabbit", "melvin", 32.53]
l4.pop(1)
print(l4)

# ------------------------------------------------------------------------
                                   #TUPLES ()
# ------------------------------------------------------------------------

#Tuples are used to store multiple iteam in a single variable 
#A tuple is a collection which is ordered and unchangeable. 

a = (1, 54.33, "Melvin", "james", 99, "rajuram", "Melvin")
count_item = a.count("Melvin") #counting the presence of the iteam in the tuple
print(count_item)

b = a = (1, 54.33, "Melvin", "james", 99, "rajuram", "Melvin")
i = a.index(99) #finding the position of the item in the tuple
print(i) 

#Practise SET

#Problem Statement 1: write a program to store 7 fruite in a list entered by the user 
fruits = []
for i in range (0,7):
    user_input = input("Enter the Name of the Fruite: ")
    fruits.append(user_input)
print(fruits)

#Problem Statement 2: write a program to store 7 Subject marks order wise and sort them accroding to higher marks
marks = []
for i in range(0,7):
    std_marks = int(input("Enter your marks: "))
    marks.append(std_marks)
marks.sort()
print(marks)

#Problem Statement 3: Check that Tupple type can not be changed 
a = (32,43, "Melvin")
# a.append(45) #this will through an error
print(a)


#Problem Statement 4: write a program to sum the number from the list

#Method2: 
numbers = [34, 66, 89, 12]
j = 0
for i in range (0, 4):
    x += numbers[i] 
print(x)

#Method1: Easy way (simple and sort)
print(sum(numbers[0:4]))