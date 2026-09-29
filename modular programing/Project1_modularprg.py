import student_report_new as sr

n=int(input("enter the number of students: "))
ns=int(input("enter the number of subjects"))

student=sr.student_details(n,ns)
total=sr.total_marks(student)
per=sr.percentage(total)
grade=sr.grade(per)
status=sr.status(grade)
sr.report_card(student,total,per,grade,status)
