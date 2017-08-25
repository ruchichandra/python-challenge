# Dependencies
import csv

# Open csv files to load
file = "RawData/election_data_2.csv"
 
# Print output to text file in Analysis folder
output = "Analysis/Election_Analysis_2.txt"
 
# Variable to track
candidates = []
candidate_votes ={}
total_votes = 0
winning_candidate = ""
winning_percentage = 0     
vote_percentage = []
        

# Reading files  
with open(file) as election_data:
    reader = csv.DictReader(election_data)
        
    for row in reader:
        # print(row)

        # Total votes
        total_votes = total_votes + 1
        
        # Building array of Unique Candidates
        if row["Candidate"] not in candidates:

            # Add the candidate and set the initial vote count to 0
            candidates.append(row["Candidate"])
            candidate_votes[row["Candidate"]] = 0

        # If candidate is not Unique
        candidate_votes[row["Candidate"]] = candidate_votes[row["Candidate"]] + 1
        
    print(candidate_votes)
    print("Election Results")
    print("------------------------")
    print("Total Votes: " +  str(total_votes))
    print("------------------------")  

    # Iterate through the candidate votes
    for candidate in candidate_votes:

        votes = candidate_votes[candidate]       
        vote_percentage = (votes / total_votes) * 100
        vote_percentage = round(vote_percentage,2)
        print(candidate + ":" + " " + str(vote_percentage * 1.00) + "%" + "       " + str(votes)) 

            
    # Find the winner and winning percentage of votes
        if (vote_percentage > winning_percentage):
            winning_candidate = candidate
            winning_percentage = vote_percentage

print("------------------------")
print("Winner: " + winning_candidate)
print("------------------------")    

# Open the output file using "write" mode.    
with open(output, 'w') as txt_file:
    txt_file.write("---------------------")
    txt_file.write("\n")
    txt_file.write("Election Results")
    txt_file.write("\n")
    txt_file.write("------------------------")
    txt_file.write("\n")
    txt_file.write("Total Votes: " + str(total_votes))
    txt_file.write("\n")
    txt_file.write("------------------------")
    txt_file.write("\n")            
    for candidate in candidate_votes:
        txt_file.write(candidate + ":" + " " + str(vote_percentage * 1.00) + "%" + "       " + str(votes))
        txt_file.write("\n")
    txt_file.write("\n")
    txt_file.write("------------------------")
    txt_file.write("\n")
    txt_file.write("Winner: "+ winning_candidate)
    txt_file.write("\n")
    txt_file.write("------------------------")
    txt_file.write("\n")

                                                    
                    
      



                


            