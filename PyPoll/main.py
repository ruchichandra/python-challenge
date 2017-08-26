# Dependencies
import csv

# Files to Load / Output
input = "RawData/election_data_1.csv"
output = "Analysis/Election_Analysis_1.txt"

# Variables to Track

candidate_options = []
candidate_votes = {}
total_votes = 0
winning_candidate = ""
winning_percentage = 0

# Reading the file
with open(input) as election_data:
  reader = csv.DictReader(election_data)

 # For Each row in reader
  for row in reader:

   # Total Votes
    total_votes = total_votes + 1

   # Build an Array of Unique Candidates
    if row["Candidate"] not in candidate_options:

     # Add the candidate as an option
      candidate_options.append(row["Candidate"])

     # Set that candidate's initial vote count to 0
      candidate_votes[row["Candidate"]] = 0

   # If the candidate is NOT unique
    candidate_votes[row["Candidate"]] =  candidate_votes[row["Candidate"]] + 1
  print()
  print('Election Results')
  print('----------------------------')
  print('Total Votes: ',total_votes )
  print('----------------------------')
  with open(output, "w") as txt_file:
    txt_file.write('Election Results')
    txt_file.write("\n")
    txt_file.write('----------------------------')
    txt_file.write("\n")
    txt_file.write('Total Votes: '+ str(total_votes))
    txt_file.write("\n")
    txt_file.write('----------------------------')
    txt_file.write("\n")
  # Iterate through the candidate_votes
  for candidate in candidate_votes:

    votes = candidate_votes[candidate]
    vote_percentage = round((votes / total_votes) * 100,2)

    print(candidate +' ' + str(vote_percentage)+'% ('+str(votes)+')')
    with open(output, "a") as txt_file:
      txt_file.write(candidate +' ' + str(vote_percentage)+'% ('+str(votes)+')')
      txt_file.write("\n")

    if(vote_percentage > winning_percentage):

      winning_candidate = candidate
      winning_percentage = vote_percentage

 # Printing The Winner
  print('----------------------------')
  print("Winner: " + winning_candidate)
  print('----------------------------')
  # Output Files
  with open(output, "a") as txt_file:
     txt_file.write('----------------------------')
     txt_file.write("\n")
     txt_file.write('Winner: ' + winning_candidate)
     txt_file.write("\n")
     txt_file.write('----------------------------')
     txt_file.write("\n")