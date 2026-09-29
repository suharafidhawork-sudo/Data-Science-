def report_card(students, total, per, gr, stat):
    names = list(students.keys())
    print("-"*50)
    for i in range(len(names)):
        print("Student Name  : ",names[i])
        print("Marks         : ",students[names[i]])
        print("Total Marks   :", total[i])
        print("Percentage    : ",round(per[i], 2))
        print("Grade         : ",gr[i])
        print("Status        : ",stat[i].upper())
        print("-"*50)