transactions_aed = [23.45, 67.89, 12.34, 78.90, 54.21, 11.22, 33.44, 55.66, 77.88, 99.00]


transactions_usd = []

i = 0

while i <= len(transactions_aed) - 1:
    item_usd = transactions_aed[i] *x§ 0.27
    print("Converting value", transactions_aed[i])
    transactions_usd.append(item_usd)
    i += 1




for transaction in transactions_aed:
    item_usd = transaction * 0.27
    print("Converting value", transaction)
    transactions_usd.append(item_usd)

# lst = [2, 4, 5, 6]

# for number in lst:
#     if number % 2 == 0:
#         print(number * 2)

# Determine the max grade

# students_data = [
# {'name': 'Alice', 'grades': [85, 88, 92], 'age': 20},
# {'name': 'Bob', 'grades': [90, 87, 80, 88], 'age': 21},
# {'name': 'Charlie', 'grades': [78, 80, 82, 77], 'age': 22}
# ]

# for student in students_data:
#     total_grades = sum(student['grades'])
#     number_of_grades = len(student['grades'])
#     average_grade = total_grades / number_of_grades
#     max_grade = max(student['grades'])

#     # Create a message about the student
#     message = f"{student['name']} is {student['age']} years old. "
#     message += f"They have an average score of {average_grade:.2f} and their highest score was {max_grade}.\\n"
#     message += "Here are their grades: \\n"

#     # Adding a nested loop to iterate over grades and create a detailed message
#     for idx, grade in enumerate(student['grades']):
#         message += f"\\t- Test {idx + 1}: {grade}\\n"

#     # Check if the student is graduating (assuming average grade above 85 is pass)
#     if average_grade > 85:
#         message += f"{student['name']} is graduating with honors!\\n"
#     else:
#         message += f"{student['name']} is graduating.\\n"

#     # Print the message
#     print(message)


# print(transactions_usd)