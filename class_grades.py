# CodeAcademy Python Class Grades
lloyd = {
    "name": "Lloyd",
    "homework":[90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}
stds = [lloyd, alice, tyler]

#Add your function below!
def average(numbers):
    #generic average to work anyhwere
    total = float(sum(numbers))/len(numbers)
    return total

def get_average(student):
    # calculate total weighted average over homework, quizzes and test
    hw = average(student['homework'])
    print 'hw average from get_average() is %d' %(hw)
    qz = average(student['quizzes'])
    ts = average(student['tests'])
    weighted_average = 0.1*hw + 0.3*qz + 0.6*ts
    return weighted_average

def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def get_class_average(students):
    results = []
    for student in students:
        x = get_average(student)
        print ('%s \' average is %d') %(student['name'], x)
        results.append(x)
        answer = get_letter_grade(x)
        print answer

get_class_average(stds)
