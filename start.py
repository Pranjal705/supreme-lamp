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
    
    #Age in Seconds
#Houseflies have an approximate life of four weeks. Given the number of days a
#housefly lived, design an algorithm and write the Python code to determine its
#approximate age in seconds. Check for boundary conditions and print ‘Invalid
#input’ if condition is not satisfied. For example, if a housefly lived for 21
#days then its approximate age in seconds is 21*24*60*60 is 1814400.

#Input Format

#Number of days, n

#Output Format

#Number of seconds

#Boundary Conditions

#n>0 and n <28

n=int(input('enter the no. of days'))
if n<0 or n>28:
    print('Invalid input')
else:
    days=n*24*60*60
    print(days)
