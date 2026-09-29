def student_details(ns,nsub):
    students=dict()
    for i in range(ns):
        name = input("enter the name: ")
        m = list()  
        for j in range(nsub):
            a = int(input("enter the marks"))
            m.append(a)
        students[name] = m
    return students
