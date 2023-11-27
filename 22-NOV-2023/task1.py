#Q1.Define five different variables showcasing various data types.Print each variable along with its data type.

#INTEGERS
'''x=10
print('value of x is:',x)
print('type of x is:',type(x))

#STRINGS
str="Hi everyone!how r u.."
print('value of str is:',str)
print('type of str is:',type(str))

#LISTS
thislist=['apple','cherry','mango']
print('list values are:',thislist)
print('type of thislist is:',type(thislist))

#TUPLES
thistuple=('sparrow','peacock','pigeon')
print('tuple values are:',thistuple)
print('type of thistuple is:',type(thistuple))

#DICTIONARIES
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print('dictionary values are:',thisdict)
print('type of thisdict is:',type(thisdict))'''


#Q2.Define and explain different data types available in python.

#INT example
'''otp=3245
print('OTP is:',otp)

#FLOAT example
pi=3.14
print('PI value is:',pi)

#STR example
str='Hello World'
print("str value is:",str)

#LIST example
fruit_list=['apple','banana','cherry']
print('fruit list:',fruit_list)

#TUPLE example
subject_tup=('maths','english','hindi')
print('subject list:',subject_tup)

#DICTIONARY example
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print('dictionary:',thisdict)'''


#Q3.Implement if..else statement to check whether a number is even or odd.

'''number=int(input('enter a number:'))
if number%2==0:
  print('The number is even')
else:
  print('The number is odd')'''

#Q4.Create a for loop that iterates through a list of numbers (e.g 1 to 10).

'''n=int(input('enter how many numbers you want to print?'))
for i in range(1,n):
  print(i)'''


#Q5.Define a function that takes two arguments and return their sum.
def fun_sum(a,b):
  return a+b
sum_int=fun_sum(10,30)
print('sum of Integer numbers is:',sum_int)

sum_float=fun_sum(10.30,30.20)
print('sum of Float numbers is:',sum_float)

sum_mix=fun_sum(20,30.4)
print('sum of both int and float is:',sum_mix)
