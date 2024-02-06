from collections import namedtuple

N = int(input())
headers = input()
print(headers)

# Create a named tuple class dynamically using the headers
Student = namedtuple('Student', headers)

students = []
for _ in range(N):
    # Create a named tuple instance for each student
    student_data = input().split()
    print(student_data)
    student = Student(*student_data)
    print(student)
    students.append(student)

# Calculate the average of the 'MARKS' field
average_marks = sum(float(i.MARKS) for i in students) / len(students)

print(f"{average_marks:.2f}")


# 5
# ID         MARKS      NAME       CLASS
# 1          97         Raymond    7
# 2          50         Steven     4
# 3          91         Adrian     9
# 4          72         Stewart    5
# 5          80         Peter      6