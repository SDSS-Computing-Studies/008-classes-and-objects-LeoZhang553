 ["English","Math","PE","Computers","History","Biology","Japanese"]
  [91, 94, 87, 99, 82, 100, 73]

      st2 = student("Joe Lunchbox","12346", 11)
    st1.getCourses( ["English","Math","Physics","Computers","Geography","Chemistry","French"] )
    st1.getGrades( [71, 98, 93, 95, 68, 81, 71])

    a1=input("course1 = ")
        a2=input("course2 = ")
        a3=input("course3 = ")
        a4=input("course4 = ")
        a5=input("course5 = ")
        a6=input("course6 = ")
        a7=input("course7 = ")
        a8=input("course8 = ")

        course=[]

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

            st1 = student("Anita Bath","91334",11)
    course=st1.inputCourses()
    grades=st1.inputGrades(course)
    st1.getCourses(course)
    st1.getGrades(grades)
    st1.average(grades)
    st1.getHonorRoll(grades)
    st1.showCourses(course)
    st1.showGrades(course,grades)