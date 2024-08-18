# Budget Data Analysis

# variables
total_months = 0
net_total = 0
previous_profit = None
changes = []
dates = []

# open csv
with open('/Users/TheHector/Desktop/Class_Requirements/python-challenge/resources/budget_data.csv', 'r') as file:
    # skip header
    next(file)
    
    for line in file:
        # split the date and profit/losses
        date, profit_loss = line.strip().split(',')
        profit_loss = int(profit_loss)
        
        # count total of months
        total_months += 1
        
        # sum net of profit/losses
        net_total += profit_loss
        
        # track profit/losses
        if previous_profit is not None:
            change = profit_loss - previous_profit
            changes.append(change)
            dates.append(date)
        
        previous_profit = profit_loss

# calculate avg change
average_change = sum(changes) / len(changes)

# find increase and decrease
greatest_increase = max(changes)
greatest_decrease = min(changes)
greatest_increase_date = dates[changes.index(greatest_increase)]
greatest_decrease_date = dates[changes.index(greatest_decrease)]

# print results
print("Budget Data Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Net Total Profit/Losses: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")
print("\n")

# Election Data Analysis

# variables
total_votes = 0
candidate_votes = {}

# open csv
with open('/Users/TheHector/Desktop/Class_Requirements/python-challenge/resources/election_data.csv', 'r') as file:
    # skip header
    next(file)
    
    for line in file:
        # split up data
        voter_id, county, candidate = line.strip().split(',')
        
        # count total number of votes
        total_votes += 1
        
        # count number of votes for each candidate
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# calcuate percentage of votes
candidate_percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}

# determine winner of vote
winner = max(candidate_votes, key=candidate_votes.get)

# print results
print("Election Data Analysis")
print("----------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------")
print("Candidates who received votes:")
for candidate in candidate_votes:
    print(f"{candidate}: {candidate_percentages[candidate]:.2f}% ({candidate_votes[candidate]} votes)")
print("----------------------------")
print(f"Winner: {winner}")