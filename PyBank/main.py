# Dependencies
import csv

# Open csv file to load
file = "RawData/budget_data_2.csv"

# Print output to text file
output = "Analysis/Budget_Analysis_2.txt"

# Read file   
with open(file, newline='') as budget_data:
    
    # CSV reader specifies delimiter and variable that holds contents
    reader = csv.DictReader(budget_data, delimiter=',')

    # Variables to track
    total_months = 0
    total_revenue = 0
    prev_revenue = 0
    revenue_change = 0
    greatest_increase = ["", 0]
    greatest_decrease = ["", 9999999999999999999999]
    revenue_changes = []

    # Loop through all the rows of data
    for row in reader:
        # print(row)

        # Calculate the totals
        total_months = total_months + 1
        total_revenue = total_revenue + int(row["Revenue"]) 
        #print(row)
        
        # Calculate Changes
        revenue_change = int(row["Revenue"]) - prev_revenue
        
        # Reset the value of prev_revenue to the analysed row 
        prev_revenue = int(row["Revenue"])

        # Calculate greatest increase and smallest decrease
        if(revenue_change > greatest_increase[1]):
            greatest_increase[1] = revenue_change
            greatest_increase[0] =row["Date"]
        
        if(revenue_change < greatest_decrease[1]):
            greatest_decrease[1] = revenue_change
            greatest_decrease[0] =row["Date"]

    # Add to the revenue_change list
    revenue_changes.append(int(row["Revenue"]))

    # Calculate the average revenue change
    avg_revenue_change  = sum(revenue_changes) / len(revenue_changes)
                
# Print output to terminal
print("---------------------")
print("Financial Analysis")
print("---------------------")
print("Total Months: " + str(total_months))
print("Total Revenue: " + "$" + str(total_revenue))
print("Average Revenue Change: " + "$" + str(avg_revenue_change))
print("Greatest Increase in Revenue: " + str(greatest_increase[0]) + " " +  "($" + str(greatest_increase[1]) + ")")
print("Greatest Decrease in Revenue: " + str(greatest_decrease[0]) + " " +  "($" + str(greatest_decrease[1]) + ")")  

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output, 'w') as txt_file:

    txt_file.write("---------------------")
    txt_file.write("\n")
    txt_file.write("Financial Analysis")
    txt_file.write("\n")
    txt_file.write("---------------------")
    txt_file.write("\n")
    txt_file.write("Total Months: " + str(total_months))
    txt_file.write("\n")
    txt_file.write("Total Revenue: " + "$" + str(total_revenue))
    txt_file.write("\n")
    txt_file.write("Average Revenue Change: " + "$" + str(avg_revenue_change))
    txt_file.write("\n")
    txt_file.write("Greatest Increase in Revenue: " + str(greatest_increase[0]) + " " +  "($" + str(greatest_increase[1]) + ")")
    txt_file.write("\n")
    txt_file.write("Greatest Decrease in Revenue: " + str(greatest_decrease[0]) + " " +  "($" + str(greatest_decrease[1]) + ")")
    txt_file.write("\n")
    

            

