# Q1.Check if a given string is palindrome or not.

'''str=input('enter a string:')
a=len(str)
b=(str[-1:-(a+1):-1])
if b==str:
    print('Palindrome')
else:
    print('Not Palindrome')'''


#Q2.Concatenate two strings into a single string.

'''str1=input('enter string1:')
str2=input('enter string2:')
concatenate=str1+str2
print('String after concatination:',concatenate)'''


#Q3.Calculate the sum of elements in a list of integers.

'''list=[10,30,40,60]
sum=0
for x in list:
    sum=x+sum
print('sum of elements is:',sum)'''


#Q4.Reverse the order of elements in a list without using reverse() method.

'''list=['Shreya',90,'Riya',80]
reverse=list[::-1]
print('Reverse order of elements is:',reverse)'''


#Q5.Sort a list of strings in ascending order.

'''str_list=['cherry','apple','pineapple','banana']
str_list.sort()
print('sorted list of strings is:',str_list)'''


#Q6.Remove the duplicates from the while preserving the order of elements.

'''list1=[1,3,5,7,89,13,5,2]
print('original list is:',list1)
unique_list=list(set(list1))
print('list without duplicates:',unique_list)'''


#Q7.Perform basic arithmetic operations using user input.

'''num1=int(input('enter number1:'))
num2=int(input('enter number2:'))
choice=int(input('Enter your choice(1/2/3/4):'))
if choice==1:
    sum=num1+num2
    print('addition is:',sum)
elif choice==2:
    sub=num1-num2
    print('subtraction is:',sub)
elif choice==3:
    multiply=num1*num2
    print('multiplication is:',multiply)
elif choice==4:
    divison=num1/num2
    print('divison is:',divison)
else:
    print('enter valid choice')'''


#Q8.Check if given number is odd or even.

'''number=int(input('enter a number:'))
if number%2==0:
  print('The number is even')
else:
  print('The number is odd')'''


#Q9.Check whether a given year is leap year or not.

'''year=int(input('Enter a year :'))
if year%4==0:
    print('Leap year')
else:
    print('not a leap year')'''


#Q10.Use logical operators to check conditions and return True or False.

x = 5
y = 10
condition1 = (x > 0) and (y > 0)
condition2 = (x > 0) or (y < 0)
condition3 = not (x < 0)
print("Condition 1:", condition1)
print("Condition 2:", condition2)
print("Condition 3:", condition3)


#Q11.Find maximum and minimum values in a list of numbers
'''list=[12,34,60,10,55,23,95]
list.sort()
print('Minimum valus is:',list[0])
print('Maximum valus is:',list[-1])'''


#Q12.Check if a string is a pangram.

'''import string
sentence = "The quick brown fox jumps over the lazy dog"
cleaned_sentence = sentence.lower().replace(" ", "")
is_pangram = set(cleaned_sentence) == set(string.ascii_lowercase)
print(f"Is the sentence a pangram? {is_pangram}")'''


#Q13.Split a string into words and count the frequency of each word.
str="Do what is right,not what is busy"
split=str.split()
print(split)




#Q14.Find the intersection of two lists.

'''list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
intersection = list(set(list1) & set(list2))
print("List 1:", list1)
print("List 2:", list2)
print("Intersection:", intersection)'''


#Q15.Create a dictionary from two lists.

'''keys = ["name", "age", "city"]
values = ["John", 25, "New York"]
my_dict = {}
for i in range(len(keys)):
    my_dict[keys[i]] = values[i]
print("Resulting dictionary:", my_dict)'''



#Q16.Check if all elements in a list are unique.

'''list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 2, 3, 4, 5]
are_elements_unique_list1 = len(list1) == len(set(list1))
print("List 1:", are_elements_unique_list1)
are_elements_unique_list2 = len(list2) == len(set(list2))
print("List 2:", are_elements_unique_list2)'''


#Q17.Merge two sorted list into a single sorted list.

'''list1=['apple','cherry','banana']
list2=['apricot','papaya','orange']
list1.sort()
list2.sort()
sorted_list=list1+list2
sorted_list.sort()
print('merge list:',sorted_list)'''


#Q18.Rotate elements in a list by specified number of positions.

'''list=[11,23,45,67,80,90]
print('original list:',list)
position=int(input('enter position you want to rotate:'))
list=list[position:]+list[:position]
print('Output of list left rotate by:',position,list)
list=list[-position:]+list[:-position3]
print('Output of list right rotate by:',position,'back to original list',list)'''


#Q19.Determine the factorial of a given number.

'''number=int(input('enter a number:'))
fact=1
for i in range(1,number+1):
    fact=fact*i
print('factorial of number is:',fact)'''


#Q20.Find second largest element in a list of numbers.

'''list=[20,60,45,80,95,65,110,100]
list.sort(reverse=True)
print('second largest element is:',list[1])'''









