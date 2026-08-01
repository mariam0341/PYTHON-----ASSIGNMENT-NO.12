from student import calculate_average, find_grade, display_result

name = "Saira"

marks = [85, 90, 88, 95, 80]

average = calculate_average(marks)

grade = find_grade(average)

display_result(name, average, grade)