# PROJECT - 1 ==> Grade Calculator

'''
Finding Student Grade and Percentage using the score
and displaying the student Name, Grade and Percentage
using user input.
'''

maxscore = int(input("Enter The Maximum Score In The Exam: "))
studentname = input("Enter The Student Name: ")
score = int(input("Enter The Score Of The Student: "))
percentage = round((score/maxscore)*100, 3)

'''
A = 100 - 90 %
B = 89 - 80 %
C = 79 - 70 %
D = 69 - 60 %
E = 59 - 0 %
'''

# Print the student name and what the grade they got and percentage scored 

if 100 >= percentage >= 90:
    print(f"{studentname} has got the Grade-A and Percentage = {percentage}")
elif 89 >= percentage >= 80:
    print(f"{studentname} has got the Grade-B and Percentage = {percentage}")
elif 79 >= percentage >= 70:
    print(f"{studentname} has got the Grade-C and Percentage = {percentage}")
elif 69 >= percentage >= 60:
    print(f"{studentname} has got the Grade-D and Percentage = {percentage}")
else:
    print(f"{studentname} has got the Grade-E and Percentage = {percentage}")
    