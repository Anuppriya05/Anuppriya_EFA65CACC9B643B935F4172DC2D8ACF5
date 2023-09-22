#
class student:
  def __init__(self,name,roll_num,cgpa):
     self.name=name
     self.roll_num=roll_num
     self.cgpa=cgpa
def sort_student(student_list):
  sorted_students=sorted(student_list, key =lambda student: student.cgpa,reverse=True)
  return sorted_students 
students=[
  student("Sreya","A111",7.5) ,
  student("Priya","A112",8.1),
  student("Anush","A115",6.9),
  student("Feroz","A114",6.7),
  student("Akash","A113",8.5) ]
sorted_students= sort_student(students)
for students in sorted_students:
  print("Name:{},Roll Number:{},Cgpa:{}".format(students.name,students.roll_num, students.cgpa))