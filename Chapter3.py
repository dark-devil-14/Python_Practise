# ------------------------------------------------------------------------
                                   #DICTIONARY AND SETS 
# ------------------------------------------------------------------------
#Dictionary is a collection which is ordered** and changeable. No duplicate members.

marks = {
    "Harry" : 100,
    "Ram" : 54,
    "Melvin" : 23,
} 

#Properties of Python Dictionaries
'''
1. It is Unordered 
2. It is Mutable (can be changed)
3. It is indexed
4. Cannot no always contain duplicate keys 
'''
#Accessing Items //Getting the complete iteams from dict 
print(marks.items()) 

#Accessing Keys // Getting only the left side string,int  
print(marks.keys()) 

#Accessing Items // Getting the right side values of key 
print(marks.values()) 

#Updating the Dict //Changing the values in a perticular key , if that key does not exisit it is automatically created
marks.update({"Harry" : 99})
marks.update({"Rajuram" : 33}) #Ceates the new Key in the dict
print(marks.items())

#get 
#what is diffrence between these 2 codes bellow both gives the same output 
print(marks.get("Rajuram")) #prints none
print(marks["Rajuram"])  #returns error
'''
Yes, Both gives the same values from the key, but if you search "rajuram2" the 
get method will give you  "None" but the simple marks["rajuram2"] will give 
the error
'''

# ------------------------------------------------------------------------
                                   #SETS 
# ------------------------------------------------------------------------
#Collection of the well defined non repitative objects.
#In set elements are not repeated, if you have same no. in a set it consider it only once 

s ={}  #dont use this , this creats an empty dict
s = set() #this also creates
s = {3, 5, 7, 15, 5, 6, 2} #even this also creates the sets
print(type(s))
print(s) 

#Properties of Python Dictionaries
'''
1. Set items are unordered, unchangeable, and do not allow duplicate values.
2. Unordered means that the items in a set do not have a defined order.
   Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
3. Set items are unchangeable, meaning that we cannot change the items after the set has been created.
4. Once a set is created, you cannot change its items, but you can remove items and add new items.
5. Note: The values False and 0 are considered the same value in sets, and are treated as duplicates:
'''

#Methods of SET (add)
s.add("Rashika") 
print(s, type(s))

#len (returns the length of the set)
print(len(s)) #7 CUZ it have 7 elements in it (repatative are considered only once)

#remove //Update and removes the set 
s.remove("Rashika") #This removes the name "Rashika" from the list
print(s)

#Pop() Removes an arbitary/Random elements from the set and return the element removed 
print(s.pop())

#Set UNION (Adds those elements in SET A from set B which is not there in A)
s1 = {1, 23, 65, 7}
s2 = {99, 122, 65, 1, 33}

print(s1.union(s2)) #Union s2 elements in s1 which is not there in set 1
print(s1.intersection(s2)) #Intersection gets the common elements which is present in both the sets

#------------------------------------ Practise SET --------------------------------------------------
#------------------------------------ Practise SET --------------------------------------------------

#Problem Statement1: Write a program to crete a dictionary of Hindi words with values as their English Translation. Provide user with an option to look it up 
words = {
    "Kaise Ho" : "How are you",
    "Khana Khaiya" : "Did You ate the food",
    "Payaar" : "Love",
    "Zindagi": "Life"
}

word = input("Enter the word you want the meaning of:  ")
print(words.get(word))

#Problem Statement 2: Write a program to input eight numbers from the user and display all the unique number once 
new_set = set()

for i in range(1,9):
    n = int(input(f"Enter the Number {i} "))
    new_set.add(int(n))
print(new_set)

#Problem Statement 3: Write a program for an empty dict. allow 4 friends to enter the fav language as value and use key as their nme. assumae that the name are unique
dict_empty = {}

for i in range(1,5):
    name = input("Enter friends name: ")
    lang = input("Enter language name: ")
    dict_empty.update({name : lang})
print(dict_empty)

