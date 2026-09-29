import grade
import percentage
import status
import student
import total
import report_card

n=int(input("enter the number of students: "))
ns=int(input("enter the number of subjects"))

student=student.s(n,ns)
total=total.total_marks(student)
per=percentage.percentage(total,ns)
grade=grade.grade(per)
status=status.status(grade)
report_card.report_card(student,total,per,grade,status)
