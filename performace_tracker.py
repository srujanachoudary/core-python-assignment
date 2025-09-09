class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def average(self):
        return round(sum(self.marks) / len(self.marks), 2)


# Input
students_data = {
    "John": [85, 78, 92],
    "Alice": [88, 79, 95],
    "Bob": [70, 75, 80]
}

# Convert dictionary into list of Student objects
students = [Student(name, marks) for name, marks in students_data.items()]

# Calculate averages
averages = {student.name: student.average() for student in students}

# Find top performer
top_student = students[0]   # assume first is top initially
for student in students[1:]:
    if student.average() > top_student.average():
        top_student = student

# Output
print("Average Marks:", averages)
print("Top Performer:", top_student.name)
