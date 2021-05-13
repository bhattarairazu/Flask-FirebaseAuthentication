for i in range(10):   #range always starts from 0 to n-1
    print(i) 

for k in range(1,4):   #it prints from 1 to 4-1
    print(k)

print("-------------------")

for j in range(1,10,2):
    print(j)


a = ["hello","how are you","who are yu","m"]
s = "m"

for s in a:
    print(s)
print("-------------------")

h_letters = []

for letters in 'human':
    h_letters.append(letters)
print(h_letters)

print("-----------")

lett = [letters for letters in 'human']  #list comprehension without using append
print(lett)

letters = list(map(lambda x:x,'human'))   #list comprehension using lambda function
print(letters)

print("------------")
even_no = list(x for x in range(20) if x % 2 == 0)  # list comprehension using condition to find even or odd

odd = [x for x in range(20) if x % 2 !=0] # finding odd no using list comprehension with condition
print(odd)

print("--------")

num = [ x for x in range(20) if x % 2 == 0 if x % 5 == 0] # nested if with list comprehension
print(num)

print("--------")

obj = ["Even" if i % 2 == 0 else "Odd" for i in range(10) ]
print(obj)

matrix = [[1,2,3],[3,4,5],[5,6,6]]
mat = [[ row[i] for row in matrix] for i in range(len(matrix))]  # transpose of matrix using list comprehension with nested loops
print(mat)

outerlist = []
for i in range(len(matrix)):    # transpose of matrix using nested loops

    matlist = []
    for row in matrix:
        matlist.append(row[i])
    outerlist.append(matlist)

print(outerlist)


# python dictionaries
print("--------dict-----------")
my_dict = {}
myd = {'raz':'hssle',1:'sksksks'}
dictfunct = dict({'h':'this'})
print(myd)
print(myd['raz'])
print(myd.get('raz'))
print(dictfunct)

print("------------")
# changing and adding dictionary elements
nedict = {'a':'hello','b':'hi','s':3}

nedict['a'] = 'razu'

nedict['b'] = 33
nedict['x'] = 'naice' #add new dictionary items key x and value naice
nedict['s'] = 'how'
print(nedict)

#Removing elemtns from dictionary

squares = {'a':'ew',2:3,'hh':333,'ii':2323}

squares.popitem() # remove last item from dictionary
print(squares)

squares.pop('a')  # remove item having key as a in dictionary
print(squares)

squares.clear() # remove all items from dictionary

print(squares)

del squares # delete square dictionary throws erros

#print(squares)

# dictionary methods

marks = {}.fromkeys(['Math','scient'],9)  # it forms a dictionary having keys as math,scient and value as 9 for both
print(marks)


for k in marks.items():  # print each element of dicitonary with key value
    print(k)

print(list(sorted(marks.keys())))  # print the keys of dictionary in asc order inside list with sorted

# dictionary comprenhension
print("------------------dictionary comprenhensions------------------")

squares = { x: x*x for x in range(2,12,3)}  # takes no from 2 to 12 with 3 increment and put the no as keys in dictionary
print(squares)


sq = { x : x*x for x in range(19) if x % 2 == 0}  # get only even element and form a dictionary
print(sq)

print( 64 in sq)  # it checks for key 64 is in sq or not

print (4 not in sq)

print( 11 in sq)

# iterating through dictionary elements
for i in sq:   # only print values of dictionary
    print(sq[i])

ss = {sq[i] for i in sq}
print(ss)

print("------convertino dict---------")

conv = {'rice':11,'food':12,'guava':22}
dollor_to_pound = 0.12

final = {i:v*dollor_to_pound for (i,v) in conv.items()}

print(final)
# which can be achieved as 
nedict = {}
for (items,value) in conv.items():
    nedict[items] = value * dollor_to_pound
print(nedict)

com = { i:v for (i,v) in conv.items() if v % 2 == 0} # print dictionary values having even no only  dictionary comprenhension with if condition
print(com)

# if else inside dictionary
coms = { i:("Even" if v%2 == 0 else "Odd") for (i,v) in conv.items()}

print(coms)

# example using filter() and lambda function in python

my_list = [1,2,4,5,5,6,6]
newl = list(filter(lambda x : (x*2),my_list))
print(newl)

# Program to filter out only the even items from a list
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x*x==25) , my_list))  # for filter we need to define the condition but for map we dont have to define the condition

print(new_list)

nn = list(map(lambda x : x*x,my_list))
print(nn)