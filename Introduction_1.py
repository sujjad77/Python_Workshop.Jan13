print("Hello World")

num1=32
num2=34

total=num1+num2
print(type(total)) #using 'type()' we can determine the class/type of the variable
print(total)

33*34 #gives the product

33**34 #gives 32 to the power 34

25/4 # gives dividend

25//4 # but use of // will give the integer value after division

product= 3*4.6

print(product)

sum = total + product #the will be of highest precision

print(sum)

st1= 'This is a string'
print(st1)

print(type(st1))

st2= "This is a string2"
print(st2)

st3= """This is
          a string3"""
print(st3)

st4="It's holiday"
print(st4)

st5='It\'s a holiday' #if the quotes are the part of the string itself then use \ to escape
print(st5)
# but if you need to print the escape sequence itself the use r as prefix

prest= r"It's 2019\01\13 today"
print(prest)

print(st1+st2) #string concatenation

print(st1*3) #string repition

name='Sujan Adhikari'
print(name)
print(name[0])
print(name[0:5])
print(name[:5])
print(name[6:])
print(name[-14:-9])
'if a string isnot assigned variables, it is regarded as a comment'

name='Sujan Adhikari'
age=19
print("My name is {} and my age is {}".format(name, age))
print("My name is {0} and my age is {1}".format(name, age))
print("My age is {1} and my name is {0}".format(name, age))
print("My name is {name} and my age is {age}".format(name="Sujan Adhikari", age=19))

#NEXT EXAMPLE
_name=input("Enter your name : ")
_age=input("Enter your age : ")

print("Your name is " + _name +" and age is " +_age)
print("Your name is {} and age is {}".format(_name,_age))
#print("Your name is {} and age is {}, {}".format(_name,_age)), this is an error, its must as follows
print("Your name is {} and age is {}, {}".format(_name,_age, "which is incorrect"))
print("Your name is {0} and age is {1}, happy birthday {0}.".format(_name,_age))
print("Your name is {name_key} and age is {age_key}".format(name_key=_name,age_key=_age))
print(f"Your name is {name} and age is {age}")

# bool() is used to give the true or false value
#if the value in () is 0 the bool gives false value and non zero value gives true value

print(bool(0))
print(bool(1))
print(bool(45))
print(bool(-98))


import keyword
print(keyword.kwlist)

print(len(keyword.kwlist))  #len returns the length of the data represented by the info. in ()

#DATA STRUCTURES
#LISTS

list1 = []
list2 = list()

#lists are mutable
list1.append(22) #append will add 22 into list1
print(list1)

#list can contain any tye of objects, e.g
list3=[22, "Python", True, 1, 0, list1, [4, 3, 2], None]
print(list3)
print(len(list3))
print(list3[2])
print(list3[-1])
# here print(list3[12]) will be an error as there are no 13(12+1) elements in the list
a=list(range(10))
print(a)
print(a[2])
print(a[-2])
print(a[2:])
print(a[:2])
print(a[2:6])
print(a[2:-2])
print(a[-6:-2])
print(a[:])
print(a[::2])
print(a[2::2])
print(a[:6:2])
print(a[2:6:2])
print(a[::-2]) 
print(a[::-1]) #this is used to reverse the order

# index(arg) method is used to find the index of an element in the list
print(list3.index(None))

subject=["Eng", "Math", "Physics"]
print(subject)
subject.append("Digital")
print(subject)

#append is used to add an element at last of the list, but use of insert enables to add at any index
subject.insert(1, "Python")
print(subject)

#we can merge two lists too, by using extend
alpha1=['a','b','c','d']
alpha2=['e','f','g']
alpha1.extend(alpha2)
print(alpha1)
ll=[1,2,3]
alpha1.extend(ll)
print(alpha1)
#this can also be done using "+" operator

ll+=alpha1
print(ll)

#the elements in list can also be thrown out using remove
cc=["kk", "mm", "jj", "jh"]
print(cc)
cc.remove("jj") # this will remove jj from cc
print(cc)

#pop can also be used inplace of remove 
cc.pop(2)
print(cc)





















      









         

