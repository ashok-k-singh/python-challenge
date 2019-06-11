# This is the second part of the Python assignment 
import os
import csv

# define the files
file_to_load = os.path.join("Resources", "election_data.csv")
output_file = os.path.join("Analysis", "PyPoll_Analysis.csv")


# define the function to print the PyPoll Analysis 
def print_analysis(vote_list):

    # initialize a dictionary to store the candidate names and their votes   
    candidate_list = {}
    win_vote = 0
    total_votes = len(vote_list)

    for candidate in vote_list:
        if candidate not in candidate_list:
            candidate_list[candidate] = 1
        else:
            candidate_list[candidate] += 1

    # print the election analysis to  the screen
    print("\n ******************************************************") 
    print(" PyPoll Election Results")
    print(f" Total Votes: {total_votes}")
    print(" ******************************************************")    

    for candidate in candidate_list:
        print(f" {candidate}:  {round(candidate_list[candidate]*100/total_votes)}%  ({candidate_list[candidate]})")
        if candidate_list[candidate] > win_vote:
            winner = candidate 
            win_vote = candidate_list[candidate] 

    print(" ******************************************************")   
    print(f" Winner: {winner}")

    # Opne the output file and write the output to the file
    with open(output_file, "w") as my_output_file:
        my_output_file.write("\n ******************************************************") 
        my_output_file.write("\n PyPoll Election Results")
        my_output_file.write(f"\n Total Votes: {total_votes}")
        my_output_file.write("\n ******************************************************")    
    
        for candidate in candidate_list:
            my_output_file.write(f"\n {candidate}:  {round(candidate_list[candidate]*100/total_votes)}%  ({candidate_list[candidate]})")
    
        my_output_file.write("\n ******************************************************")   
        my_output_file.write(f"\n Winner: {winner}")
        my_output_file.close()


# Initialize the candidate list
candidates_vote = []

#open the data file and read using csv reader
with open(file_to_load, newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)

    for row in csv_reader:
        candidates_vote.append(row[2])

    # Call the Print Analysis Function    
    print_analysis(candidates_vote)
