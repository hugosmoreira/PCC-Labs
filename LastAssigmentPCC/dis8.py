#******************************************************************************
# Author:           Hugo Moreira
# Lab:              Discussion 8
# Date:             8/17/2023
# Description:      This program collects candidates' names and their vote counts.
#                   After collecting all data, it calculates the percentage of votes
#                   each candidate received and declares a winner.
#                   
# Input:            Candidate names and their corresponding vote counts.
# Output:           List of candidates, their vote counts, percentages, and the winner.
# Sources:          Discussion 8 specifications
#
#
#******************************************************************************


def main():
    # Initializing the lists to hold candidate names and their votes
    candidate_names = []
    candidate_votes = []

    # Start input process
    while True:
        # Prompt for names and votes
        name, votes = get_input()
        
        candidate_names.append(name)
        candidate_votes.append(votes)

        # Ask if more candidates are there
        more = input("More candidates (y/n)? ")
        while more.lower() not in ['y', 'n']:
            print("Invalid input. Enter 'y' or 'n'.")
            more = input("More candidates (y/n)? ")

        if more == 'n':
            break

    total_votes = sum(candidate_votes)
    print_results(candidate_names, candidate_votes, total_votes)


def get_input():
    """Function to get candidate's name and vote count."""
    name = input("Enter candidate name: ")

    while True:
        try:
            votes = int(input(f"Enter number of votes for {name}: "))
            if votes < 0:
                raise ValueError
            return name, votes
        except ValueError:
            print("Invalid input. Enter a non-negative integer for votes.")


def print_results(names, votes, total_votes):
    """Function to print the results including the winner."""
    print("\nResults")
    print("Candidate   # Votes    % Votes")
    print("------------------------------")
    
    # Find the index of the maximum votes
    max_index = votes.index(max(votes))

    for i in range(len(names)):
        percentage = (votes[i] / total_votes) * 100
        print(f"{names[i]:<10} {votes[i]:<10} {percentage:.2f}%")
    
    print("\nAnd the winner is ....", names[max_index], "!\n")


if __name__ == "__main__":
    main()
