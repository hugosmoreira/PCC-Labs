
#******************************************************************************
# Author:           Hugo Moreira
# Lab:              Lab3
# Date:             7/18/2023
# Description:      Estimated calories burned per minute for each exercise type
#                   prints a message to the screen.
# Input:            Exercise type, Duration of exercise
# Output:           If a recognized exercise type is provided, the output is a printed statement indicating the number of calories burned if not "Sorry, that exercise type is not recognized by this program."
# Sources:          Lab 3 specifications
#
#
#******************************************************************************

"""
Sample Run:
-----------
Please enter the type of exercise (biking, running, swimming, yoga, jiujitsu): running
Please enter the number of minutes you exercised: 60
You have burned approximately 684.00 calories by doing running for 60.0 minutes.


"""


# Constants can be declared outside of main()
calories_per_minute = {
    "biking": 8.5,
    "running": 11.4,
    "swimming": 7.3,
    "yoga": 3.2,
    "jiujitsu": 5.5,
}

def get_exercise_type():
    """
    Gets the type of exercise from the user and returns it.
    If the input is not recognized, prompts the user to re-enter.
    """
    while True:
        exercise_type = input(
            "Please enter the type of exercise "
            "(biking, running, swimming, yoga, jiujitsu): "
        )
        if exercise_type in calories_per_minute:
            return exercise_type
        else:
            print("Sorry, that exercise type is not recognized. Please try again.")

def get_minutes():
    """
    Gets the number of minutes exercised from the user and returns it.
    If the input is not a positive number, prompts the user to re-enter.
    """
    while True:
        minutes = float(input("Please enter the number of minutes you exercised: "))
        if minutes > 0:
            return minutes
        else:
            print("Please enter a positive number for the minutes.")

def calculate_calories_burned(exercise_type, minutes):
    """
    Calculates and returns the number of calories burned 
    based on exercise type and duration.
    """
    calories_burned = minutes * calories_per_minute[exercise_type]
    return calories_burned

def print_calories_burned(calories_burned, exercise_type, minutes):
    """
    Prints the number of calories burned.
    """
    print(
        "You have burned approximately {:.2f} calories by doing {} for {} minutes."
        .format(calories_burned, exercise_type, minutes)
    )

def main():
    """
    Main function that calls other functions to get input, 
    process data, and produce output.
    """
    exercise_type = get_exercise_type()
    minutes = get_minutes()
    calories_burned = calculate_calories_burned(exercise_type, minutes)
    print_calories_burned(calories_burned, exercise_type, minutes)

# Call main function
if __name__ == "__main__":
    main()
