from IPython.display import display, Markdown
import numpy as np
import os

def check_ans(student_answer, value, message):
    if student_answer == value:
        display(Markdown(message))
    return student_answer == value

def correct(student_ans, ans, message):
    path = os.getcwd()
    #display feedback and return object if it's a student file
    if path[-7::] == 'student':
        if student_ans == ans:
            display(Markdown(message))
            return Markdown(message)
        else:
            print("Please assign your answer to the variable provided!")
    else:
    #only display feedback if master file - test automatically returns object
        display(Markdown(message))

def array_in_array(student_answer, message):
    if type(student_answer[0]) == np.ndarray:
        display(Markdown(message))
    return type(student_answer[0]) == np.ndarray

def in_array(student_answer, value, message):
    if value in student_answer:
        display(Markdown(message))
    return value in student_answer
