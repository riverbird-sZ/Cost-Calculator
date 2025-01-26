# Importing modules and creating variables
names = []
expenses = []

# Enter the number of participants 

numberOfParticipants = int(input("Enter the number of people: "))

# Adding the names of participants and their expenses

for _ in range(numberOfParticipants): 
        name = input("Enter a name: " )
        expense = float(input("Enter a cost: "))
        names.append(name)
        expenses.append(expense)
     
print(expenses)
print("This is the list of participants: " + str(names))
print("This is the list of their expenses: " + str(expenses))


# Creating a dictionary from two lists 

myFirstDictionary = dict(zip(names, expenses))
print("These are participants and their expense: ", myFirstDictionary)


# Calculating total and average expense 

totalExpenses = sum(expenses)
print("Total expense is:", totalExpenses)
averageExpense = totalExpenses / numberOfParticipants
print("Average expense is: ", averageExpense)


# Creating a dictionary to know reimbursement information 

balances = {person: expenses[i] - averageExpense for i, person in enumerate(names)}
print("Balance is: ", balances)


# Division of cost so that all participants have same expense

for x, y in balances.items():
    if y < 0:
        print(f"Someone owes to {x} {abs(y)} EUR")
    elif y > 0:
        print(f"{x} owes to someone {y} EUR")
    else:
        print(f"No one owes to {x}, niether this person owes to someone")  
        
        
# check the logic of this component
# utvrditi ko je someone










