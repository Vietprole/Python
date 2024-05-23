import re

def is_valid_student_id(student_id):
    pattern = r'^102(1[7-9]|20|21)(0[0-9]{2}[0-9]|[1-9][0-9]{2})$'
    return bool(re.match(pattern, student_id))

N = int(input())
for _ in range(N):
    student_id = input()
    print(is_valid_student_id(student_id))