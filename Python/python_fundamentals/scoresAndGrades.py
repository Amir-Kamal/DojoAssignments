from random import *

def scores():
    print("Scores and Grades")
    for i in range(10):
        score = randint(60, 100)
        grade = "N/A"
        if 60 <= score <= 69:
            grade = "D"
        elif 70 <= score <= 79:
            grade = "C"
        elif 80 <= score <= 89:
            grade = "B"
        elif 90 <= score <= 100:
            grade = "A"
        print("Score: {}; Your grade is {}".format(score, grade))
    print("End of the program. Bye!")

scores()
            
