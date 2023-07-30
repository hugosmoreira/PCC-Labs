
#******************************************************************************
# Author:           Hugo Moreira
# Lab:              Lab5
# Date:             7/29/2023
# Description:      Estimated calories burned per minute for each exercise type
#                   prints a message to the screen.
# Input:            Exercise type, Duration of exercise
# Output:           If a recognized exercise type is provided, the output is a printed statement indicating the number of calories burned if not "Sorry, that exercise type is not recognized by this program."
# Sources:          Lab 5 specifications
#
#
#******************************************************************************

"""
Sample Run:
-----------
Please enter the type of exercise (biking, running, swimming, yoga, jiujitsu): running
Please enter the number of minutes you exercised: 30
You have burned approximately 342.00 calories by doing running for 30.0 minutes.
Do you want to run the program again? (y/n): y


"""

# Constants can be declared outside of main()
CALORIES_PER_MINUTE = {
    "biking": 8.5,
    "running": 11.4,
    "swimming": 7.3,
    "yoga": 3.2,
    "jiujitsu": 5.5,
}

def get_continue_input():
    """
    Asks the user if they want to continue the program and returns their response.
    """
    while True:
        continue_input = input("Do you want to run the program again? (y/n): ").lower()
        if continue_input in ['y', 'n']:
            return continue_input
        else:
            print("Invalid input. Please enter 'y' for yes and 'n' for no.")

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
        if exercise_type in CALORIES_PER_MINUTE:
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
    calories_burned = minutes * CALORIES_PER_MINUTE[exercise_type]
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
    while True:
        exercise_type = get_exercise_type()
        minutes = get_minutes()
        calories_burned = calculate_calories_burned(exercise_type, minutes)
        print_calories_burned(calories_burned, exercise_type, minutes)

        # Check if user wants to continue
        if get_continue_input() == 'n':
            break

# Call main function
if __name__ == "__main__":
    main()
