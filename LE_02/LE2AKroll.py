# Name: Andrew Kroll
# Date: 2020-09-10
# Course-Section/LE#: CS1120-951 LE1
# Description: Calculates rainfall totals, and averages. Finds highest and
#              lowest rainfall months.


def asterisk():
    for i in range(5, 0, -1):
        for a in range(i):
            print("* ", end='')
        print()


def drivers_license_exam():
    answers = ["A", "C", "A", "A", "D", "B", "C", "A", "C", "B",
               "A", "D", "C", "A", "D", "C", "B", "B", "D", "A"]
    student_answers = []

    with open("student_answers.txt", 'r') as file:
        for student in file:
            student_answers.append(student.replace("\n", ""))

    for i in range(len(student_answers)):
        score = 0
        incorrect = []
        for a in range(len(student_answers[i])):
            if student_answers[i][a] == answers[a]:
                score += 1
            else:
                incorrect.append(a)
        if score >= 15:
            print("Student #{} passed. {} correct. {} incorrect."
                  .format(i+1, score, 20 - score))
        else:
            print("Student #{} failed. {} correct. {} incorrect."
                  .format(i+1, score, 20 - score))
        if len(incorrect) > 0:
            print("  Incorrect questions: {}".format(incorrect))


drivers_license_exam()
