#Q1.Create a python class 'Student' with attributes like 'name','age' and 'grade'.
# Include a method to display student information.

'''class Student:
      Student_name='Shreya Jain'
      Student_age=21
      Student_grade='A'
      def display(self):
         print('Student name is:',self.Student_name)
         print('Student age is:', self.Student_age)
         print('Student grade is:',self.Student_grade)
s1=Student()
s1.display()'''


#Q2.Instantiate multiple 'Student' objects and showcase their attributes and methods.

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

# Instantiate multiple Student objects
student1 = Student("Alice", 18, "A")
student2 = Student("Bob", 17, "B")
student3 = Student("Charlie", 19, "C")

# Display information about each student
student1.display_info()
student2.display_info()
student3.display_info()


#Q3.Implement a 'Book' class that stores 'title','author', and 'pages'attributes using constructor method.

'''class Book:

  def __init__(self,title,author,pages):
      self.title=title
      self.author=author
      self.pages=pages

  def display(self):
      print('Book title is:',self.title)
      print('Book author is:',self.author)
      print('Book pages:',self.pages)

b1=Book('Gitanjali','Rabindranath Tagore',1000)
b1.display()'''