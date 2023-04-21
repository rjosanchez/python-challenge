# Modules
import os 
import csv 

# Path to collect data from the resource folder
csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvfile, None)
   
# Initiatlize lists
    voters = []
    candidates = []

    for row in csvreader: 
        # Set the location of the data
        voter = row[0]
        candidate = row[2]
        
        # Add items in each row to the data lists
        voters.append(voter)
        candidates.append(candidate)

    # calculate total votes     
    totalvotes = len(voters)
    

# Get the list of candidates who received votes
    # Initialize a new list for unique candidates
    uniquecandidates = []

    # Loop through candidates list and pull out the unique values
    for x in candidates:
        if x not in uniquecandidates: 
            uniquecandidates.append(x)

# Calculate percentage of votes won by each candidate
    # formula = total of specific candidate votes (len) divided by total of all votes (totalvotes)
    #   multiplied by 100
    # Get the len for each candidate
    # Loop through candidates, if row x is equal to row x then

    Stockham = []
    for st in candidates:
        if st == uniquecandidates[0]: 
            Stockham.append(st)
    totalst = len(Stockham)
    percentst = totalst/totalvotes*100
    percentst = round(percentst, 3)

    DeGette = []
    for de in candidates:
        if de == uniquecandidates[1]: 
            DeGette.append(de)
    totalde = len(DeGette)
    percentde = totalde/totalvotes*100
    percentde = round(percentde, 3)

    Doane = []
    for do in candidates:
        if do == uniquecandidates[2]: 
            Doane.append(do)
    totaldo = len(Doane)
    percentdo = totaldo/totalvotes*100
    percentdo = round(percentdo, 3)

    finalvotes = [totalst, totalde, totaldo]
    winner = max(finalvotes)

    if winner == totalst: 
        winnername = uniquecandidates[0]
    
    elif winner == totalde:
        winnername = uniquecandidates[1]

    elif winner == totaldo:
        winnername = uniquecandidates[2]

    # Print Election Analysis
    print ("Election Results")
    print ("------------------------------")
    print (f"Total Votes: " + str(totalvotes))
    print ("------------------------------")
    print (uniquecandidates[0] + ": " + str(percentst) + "% " + "(" + str(totalst) + ")")
    print (uniquecandidates[1] + ": " + str(percentde) + "% " + "(" + str(totalde) + ")")
    print (uniquecandidates[2] + ": " + str(percentdo) + "% " + "(" + str(totaldo) + ")")
    print ("------------------------------")
    print (f"Winner: " + winnername)
    print ("------------------------------")

report = open('election-analysis.txt', 'w')
report.write ("Election Results" + '\n')
report.write ("------------------------------" + '\n')
report.write (f"Total Votes: " + str(totalvotes) + '\n')
report.write ("------------------------------" + '\n')
report.write (uniquecandidates[0] + ": " + str(percentst) + "% " + "(" + str(totalst) + ")" + '\n')
report.write (uniquecandidates[1] + ": " + str(percentde) + "% " + "(" + str(totalde) + ")" + '\n')
report.write (uniquecandidates[2] + ": " + str(percentdo) + "% " + "(" + str(totaldo) + ")" + '\n')
report.write ("------------------------------" + '\n')
report.write (f"Winner: " + winnername + '\n')
report.write ("------------------------------")
report.close()
    



    
    



