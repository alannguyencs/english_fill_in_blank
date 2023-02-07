from constants import *
import text

text.write_questions()
submission = input("Submission: ")
if submission:
    text.show_result()