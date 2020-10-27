#! python3
"""
(10 points) 
Create a class object for a student.
It should have the following properties
str name
str studentNumber
int grade
list courses - to corresepond with course names
list grades - to correspond with grades

It should have the following methods:
average()       - determines the mathematical average of all course grades
getHonorRoll()  - determines the average of the top 5 courses if there are at least 5 courses.
                  returns True if the average is 86 or higher (on the honor roll)
                  returns False if not on the honor roll
showCourses()   - prints a list of all courses
showGrade(int)  - takes 1 parameter, the index of the list
                - displays the course name and grade
getCourses(list)- Receives a list of courses and stores that in the class property
getGrades(list) - Receives a list of grades and stores that in the class property
constructor     - should require the student name, studentNumber and grade (in that order)
"""

class student:
    # properties should be listed first
    name=''
    number=''
    grade=0


    def __init__(self,name,number,grade):
        # You will need to create your own input parameters for all methods
        self.name=name
        self.number=number
        self.grade=grade

        print('Student name is '+self.name)
        print('His/her student number is '+self.number)

    def inputCourses(self):

        print("enter your course grades")
        print("===============================================")

        course=[]
        i=0

        while i<7:
            a=input("course = ")
            if a != "0":
                course.append(a)
            i+=1

        return course

    def getCourses(self,course):
        self.course=course

    def inputGrades(self,course):
        num=len(course)
        i=0
        print("enter your course grades")
        print("===============================================")
        grades=[]
        while i<num:
            a=input("course grade= ")
            a=int(a)
            grades.append(a)
            i += 1

        return grades

    def getGrades(self,grades):
        self.grades=grades

    def average(self,grades):
        num=len(grades)
        num=int(num)
        i=0
        a=0
        while i<num:
            a += grades[i]
            i += 1
        average=a/num
        average=str(average)
        print("average= "+average)
        return average

    def getHonorRoll(self,grades):
        grades.sort()
        ave5=(grades[-1]+grades[-2]+grades[-3]+grades[-4]+grades[-5])/5
        if ave5 >= 86:
            print("Honor Roll")
            return True
        else:
            return False
        
    def showCourses(self,course):
        print(course)

    def showGrades(self,course,grades):
        index=input("input an index: ")
        index=int(index)
        print(course[index])
        print(grades[index])

    def __del__(self):
        print("END")


def main():
    # This contains test data that will be used by the autograder.
    # do not modify this function

    st1 = student("Anita Bath","91334",11)
    course=st1.inputCourses()
    grades=st1.inputGrades(course)
    st1.getCourses(course)
    st1.getGrades(grades)
    st1.average(grades)
    st1.getHonorRoll(grades)
    st1.showCourses(course)
    st1.showGrades(course,grades)

main()