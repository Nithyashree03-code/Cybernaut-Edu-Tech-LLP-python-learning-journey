name = input("Enter the student's name: ")
student_class = input("Enter the class: ")
section = input("Enter the section: ")
marks = []
for i in range(5):
    mark = float(input(f"Enter marks for subject {i + 1}: "))
    marks.append(mark)
total_marks = sum(marks)
percentage = (total_marks / 500) * 100  # Total possible marks for 5 subjects is 500
print(f"\nName: {name}")
print(f"Class: {student_class}")
print(f"Section: {section}")
print(f"Total Marks: {total_marks}")
print(f"Percentage: {percentage:.2f}%")
