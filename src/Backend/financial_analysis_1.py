
import pandas as pd

def track_finances(data_frame):
    # Calculate sum of income
    total_income = data_frame[data_frame['Type'] == 'Income']['Amount'].sum()
    
    # Calculate sum of expenses
    total_expense = data_frame[data_frame['Type'] == 'Expense']['Amount'].sum()
    
    # Calculate net profit or loss
    net_profit_loss = total_income - total_expense
    
    return total_income, total_expense, net_profit_loss

# Sample Data
data = {
    'Type': ['Income', 'Expense', 'Income', 'Expense'],
    'Amount': [2000, 500, 1500, 300]
}

df = pd.DataFrame(data)

# Uncomment the following line to run the function
# print(track_finances(df))
