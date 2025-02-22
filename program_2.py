# Program #2: Math Quiz
# Write a program that gives simple math quizzes.  The program should display two random numbers to be added, such as

#     247

# + 129

# ------
import random

def student_quiz():
    n1=random.randint(1,300)
    n2=random.randint(1,300)

    print(f"{n1}\n+{n2}\n------")

    student_input=int(input("Answer:"))

    solution=n1+n2

    if student_input==solution:
        print("Correct, nice job!")
    else:
        print(f"Not quite, the correct answer is {solution}.")

student_quiz()
# The program should allow the student to enter the answer.  
# If the answer is correct, a message of congratulations should be displayed.  
# If the answer is incorrect a message showing the correct answer should be displayed.  
# The program must use a function that accomplishes part of the needed tasks.
