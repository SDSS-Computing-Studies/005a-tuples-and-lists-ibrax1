#!python3

"""
Create a variable that contains an empy list.
Ask a user to enter 5 words.  Add the words into the list.
Print the list
inputs:
string 
string
string
string
string

outputs:
string

example:
Enter a word: apple
Enter a word: worm
Enter a word: dollar
Enter a word: shingle
Enter a word: virus

['apple', 'worm', 'dollar', 'shingle', 'virus']
"""
a = input("Enter a word: ")
b = input("Enter a word: ")
c = input("Enter a word: ")
d = input("Enter a word: ")
e = input("Enter a word: ")
list = []
list.append(a)
list.append(b)
list.append(c)
list.append(d)
list.append(e)
print(list)