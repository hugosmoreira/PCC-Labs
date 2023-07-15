#******************************************************************************
# Author:           Hugo Moreira
# Lab:              Lab2
# Date:             7/8/2023
# Description:      Estimated calories burned per minute for each exercise type
#                   prints a message to the screen.
# Input:            input string, input float
# Output:           You have burned approximately {:.2f} calories by doing {} for {} minutes.
# Sources:          Lab 2 specifications
#
#
#******************************************************************************






calories_per_minute = {
    "biking": 8.5,
    "running": 11.4,
    "swimming": 7.3,
    "yoga": 3.2,
    "jiujitsu": 5.5,
}

exercise_type = input("Please enter the type of exercise (biking, running, swimming, yoga, jiujitsu): ")
minutes = float(input("Please enter the number of minutes you exercised: "))

if exercise_type in calories_per_minute:
    calories_burned = minutes * calories_per_minute[exercise_type]
    print("You have burned approximately {:.2f} calories by doing {} for {} minutes.".format(calories_burned, exercise_type, minutes))
else:
    print("Sorry, that exercise type is not recognized by this program.")
