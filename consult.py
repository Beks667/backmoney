# a = [ 5, 3, 8, 13, 5, 6, 8, 15, 13, 5, 5, 8, ]
# a.sort()
# b= (list(set(a)))
# c=b.copy()
# c.append(b)
# print(c)

# ========================================================================================================

# datebase_d = {'admin': 'pass123' , 'Jack': 'super007', 'Adele': 'singer1995'}

# attepmts_c = 0 

# login_i = input("Login:") 

# if login_i not in datebase_d.keys(): 
# 	print("No such login.")
# else:
# 	while(True):
# 		password_i = input("Password:") 
# 		if password_i != datebase_d[login_i]: 
# 			print("Incorrect password")
# 			attepmts_c += 1 
# 		else: 
# 			print(f'Greetings, {login_i}!')
# 			break

# 		if(attepmts_c >= 3): 
# 			print("3 attepmts used. Try again later.")
# 			break
# ==================================================================================================================   

# jrnl={
#     'Tom':[24,20,100,87,64],
#     'Beks':[18,99,28,95,100],
#     'Bob':[67,65,87,23,40],
#     'Mari':[55,37,84,93.22],
#     'John':[87,65,91,11,24]

# }

# best_student_name =''
# all_avg_grade_student={}
# best_grade_student=0
# for student,grade in jrnl.items():
#     all_avg_grade_student[student]=sum(grade) / len(grade)
#     for best_grade in all_avg_grade_student.values():
#         if best_grade > best_grade_student:
#             best_grade_student=best_grade
#             best_student_name=student

# best_name={best_student_name:best_grade_student}
# print(best_name)
# print(all_avg_grade_student)














