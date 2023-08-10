#******************************************************************************
# Author:           Hugo Moreira
# Lab:              Lab7
# Date:             8/10/2023
# Description:      This program analyzes death penalty statistics for various US states.
#                   It calculates the percentage of death sentences that resulted in exonerations
#                   and compares the expected and actual exonerations for the top 5 states with the
#                   highest number of death sentences.
# Input:            Data on death sentences, exonerations, inmates, and executions for various US states.
# Output:           Nationwide percentage of death sentences resulting in exonerations and a table
#                   comparing expected and actual exonerations for the top 5 states.
# Sources:          Lab 7 specifications, Death Penalty Information Center Fact Sheet
#
#
#******************************************************************************


class State:
    __name = ""
    __abbrev = ""
    __exoneration = 0
    __inmates = 0
    __executions = 0
    __sentences = 0

    def __init__(self, name, abbrev, exonerate, inmates, executions, sentences):
        self.__name = name
        self.__abbrev = abbrev
        self.__exoneration = exonerate
        self.__inmates = inmates
        self.__executions = executions
        self.__sentences = sentences

    def exonerations_per_sentence(self):
        return self.__exoneration / self.__sentences

    def get_name(self):
        return self.__name

    def get_abbrev(self):
        return self.__abbrev

    def get_sentences(self):
        return self.__sentences

    def get_exonerations(self):
        return self.__exoneration

def make_data():
    data = [
        State("Florida", "FL", 28, 354, 94, 965),
        State("Illinois", "IL", 21, 0, 12, 304),
        # ... [rest of the states data remains unchanged]
    ]
    return data

def calc_percent_exonerations(states):
    total_exonerations = 0
    total_sentences = 0

    for state in states:
        total_exonerations = total_exonerations + state.get_exonerations()
        total_sentences = total_sentences + state.get_sentences()

    return 100 * total_exonerations / total_sentences

def get_sentences(state):
    return state.get_sentences()

def main():
    states = make_data()

    # Sort states in descending order by number of death sentences
    states.sort(key=get_sentences, reverse=True)
    percent_exonerated_sentences = calc_percent_exonerations(states)

    print("Nationwide, {:.2f}% of death sentences handed out resulted in exonerations.".format(percent_exonerated_sentences))
    print("For the 5 states in the US with the highest number of death sentences handed")
    print("out, here are the expected and actual number of exonerations:")
    print()
    print("State Name      Sentences    Exonerated    Expected Exonerations    Difference")
    print("==========      =========    ==========    =====================    ==========")

    for i in range(5): # Display data for top 5 states
        state = states[i]
        sentences = state.get_sentences()
        actual_exonerations = state.get_exonerations()
        expected_exonerations = percent_exonerated_sentences * sentences / 100
        # Fix: Round the expected exonerations to the nearest whole number
        expected_exonerations = round(expected_exonerations)  # <-- CHANGED HERE
        difference = expected_exonerations - actual_exonerations
        print(
            "{:15s}".format(state.get_name()),
            "{:6d}".format(sentences),
            "{:12d}".format(actual_exonerations),
            "{:19d}".format(int(expected_exonerations)),
            "{:19d}".format(int(difference))
        )

main()
