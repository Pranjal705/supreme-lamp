print('Hello world')
#Distinct Letter
#A word is called as a good word if all the letters of the word are distinct.
#That is, all the letters of the word are different from each other letter.
#Else, the word is called as a bad word.

#Write an algorithm and the subsequent Python code to check if the given word is
#good or bad.: e.g. START, GOOD, BETTER are bad: WRONG is good! Make the
#comparison to be case insensitive.

#Input format:

#A word

#Output format:

#Print ‘Good’ if all letters of the word are distinct and print ‘bad’ otherwise

n=input('enter a word')
l=n.casefold()
list1=[]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]==l[j]:
            list1.append(i)
            break
if list1!=[]:
    print('Bad word')
else:
    print('Good word')
    
    #Keyboard Letters
#Given an  English word,  write an algorithm and the subsequent Python code to
#check if the given word can be typed using just a single row of the keyboard.
#(e.g. POTTER, EQUITY). Print 'Yes' if the letters of the word are from a single
#row and print 'No' otherwise.

#Input format:

#A word

#Output format:

#Print ‘Yes’ if all letters of the word are from same row in a keyboard
list1=['Q','W','E','R','T','Y','U','I','O','P','q','w','e','r','t','y','u','i','o','p']
list2=['A','S','D','F','G','H','J','K','L','a','s','d','f','g','h','j','k','l']
list3=['Z','X','C','V','B','N','M','z','x','c','v','b','n','m']
row1=set(list1)
row2=set(list2)
row3=set(list3)
n=input('enter the word')
list4=[]
for i in n:
    list4.append(i)
a=set(list4)
if a.issubset(row1):
    print('Yes')
elif a.issubset(row2):
    print('Yes')
elif a.issubset(row3):
   print('Yes')
else:
    print('No')
