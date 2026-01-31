# "Ths tsk wll reqir you t rmove vwels frm a txt."
# takes user input as a string
# ● remove vowels from the string (take care if it is single character)
# ● output the vowel stripped string
# The program should exit on typing q. Save the script as

while(1):
    words = input("Enter the Letter: ")
    lis_words = list(words)
    new_lis = " "

    if (words == 'q'):
        break       
    for x in lis_words:
        if x.lower() not in ['a', 'e', 'i', 'o', 'u']:
                new_lis += x

    print(new_lis)