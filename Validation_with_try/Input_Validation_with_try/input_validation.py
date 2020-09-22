"""
Program: test_validation_with_try
Author: Ihsanullah Anwary
Last date modified: 09/21/2020
This program  allows user to enter scores and output the average with validation try.
"""


def average():  # Function definition.
    # user inputs
    score_1 = int(input(" Enter the first score"))
    if score_1 < 0:
        raise ValueError("validated")
    score_2 = int(input(" Enter the second score"))
    if score_2 < 0:
        raise ValueError("validated")
    score_3 = int(input("Please enter third score: "))
    if score_3 < 0:
        raise ValueError("validated")
    total_score = int(3)  # variable declaration.
    total_average = float(score_1 + score_2 + score_3) / total_score  # average calculation
    print(total_average)  # output the result
    return total_average  # return statement.


if __name__ == '__main__':
    average()
