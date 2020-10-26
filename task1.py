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
    course=[]
    grades=[]

    def __init__(self,name,number,grade,course,grades):
        # You will need to create your own input parameters for all methods
        self.name=name
        self.number=number
        self.grade=grade
        self.course=course
        self.grades=grades

        print('Student name is '+self.name)
        print('His/her student number is '+self.number)

    def getCourses(self):

        print("enter your course grades")
        print("enter none if you do not have any more courses")
        print("===============================================")

        a1=input("course1 = ")
        a2=input("course2 = ")
        a3=input("course3 = ")
        a4=input("course4 = ")
        a5=input("course5 = ")
        a6=input("course6 = ")
        a7=input("course7 = ")
        a8=input("course8 = ")

        if a1 != "none":
            course.append(a1)
        if a2 != "none":
            course.append(a2)
        if a3 != "none":
            course.append(a3)
        if a4 != "none":
            course.append(a4)
        if a5 != "none":
            course.append(a5)
        if a6 != "none":
            course.append(a6)
        if a7 != "none":
            course.append(a7)
        if a8 != "none":
            course.append(a8)

        return course


    def getGrades(self,course):

        num=len(course)
        num=int(num)
        i=0
        print("enter your course grades")
        print("===============================================")
        while i<num:
        a=input("course grade= ")
        a=int(a)
        grades.append(a)
        i += 1

        return grades

    def average(self,grades):
        num=len(grades)
        num=int(num)
        i=0
        a=0
        while i<num:
            a += grades[i]
            i += 1
        average=a/8
        return average

    def getHonorRoll(self,grades):
        grades.sort()
        ave5=(grades[-1]+grades[-2]+grades[-3]+grades[-4]+grades[-5])/5
        if ave5 >= 86:
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

    def __del__():
        print("END")


def main():
    # This contains test data that will be used by the autograder.
    # do not modify this function

    st1 = student("Anita Bath","91334",11)
    st1.getCourses( ["English","Math","PE","Computers","History","Biology","Japanese"] )
    st1.getGrades( 91, 94, 87, 99, 82, 100, 73)

    st2 = student("Joe Lunchbox","12346", 11)
    st1.getCourses( ["English","Math","Physics","Computers","Geography","Chemistry","French"] )
    st1.getGrades( 71, 98, 93, 95, 68, 81, 71)



grades=getGrades
course=getCourse
main()