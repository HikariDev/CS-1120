# Name: Andrew Kroll
# Date: 2020-09-10
# Course-Section/LE#: CS1120-951 LE2
# Description: Grades drivers license exams from the provided
#              student_answers.txt file.

def main():
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


main()
