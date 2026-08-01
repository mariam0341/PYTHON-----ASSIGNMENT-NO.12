def calculate_average(marks_list):
    return sum(marks_list) / len(marks_list)

def find_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    else:
        return "Fail"

def display_result(name, average, grade):
    print("Student Name:", name)
    print("Average:", average)
    print("Grade:", grade)