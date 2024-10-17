#Personal Expense Tracker Project Using Python

import csv  # Module for reading and writing to CSV files
import datetime  # For working with dates
import os  # Module to check file existence
import matplotlib.pyplot as plt  # For plotting expense data

# File to store expenses
EXPENSE_FILE = 'expenses.csv'

# Function to add expense
def add_expense():
    """
    Allows the user to input an expense with amount, category, and date.
    Stores this data in the CSV file for future access.
    """
    # User inputs for expense details
    amount = float(input("Enter the amount: $"))
    category = input("Enter the category (e.g., Food, Transport, Entertainment): ")
    date = input("Enter the date (YYYY-MM-DD) or press Enter for today: ")
    
    # If no date is provided, use the current date
    if not date:
        date = str(datetime.date.today())
    
    # Open the CSV file in append mode to add a new expense
    with open(EXPENSE_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([amount, category, date])
    print("Expense added successfully!\n")

# Function to view summaries of expenses
def view_summary():
    """
    Displays different types of summaries (by category, total spending, or monthly).
    First loads the expense data from the CSV file.
    """
    expenses = load_expenses()  # Load existing expenses from file
    if not expenses:
        print("No expenses to display.")
        return

    # User chooses the type of summary they want
    print("\nChoose summary type:")
    print("1. Total spending by category")
    print("2. Total overall spending")
    print("3. Spending over time (monthly)")

    choice = int(input("Enter your choice: "))
    
    # Call the appropriate summary function based on user input
    if choice == 1:
        category_summary(expenses)
    elif choice == 2:
        total_spending(expenses)
    elif choice == 3:
        spending_over_time(expenses)
    else:
        print("Invalid choice.\n")

# Function to load expenses from the CSV file
def load_expenses():
    """
    Reads the expenses from the CSV file and returns them as a list of dictionaries.
    Each dictionary contains amount, category, and date for an expense.
    """
    expenses = []  # List to store all expenses
    if os.path.exists(EXPENSE_FILE):  # Check if the CSV file exists
        with open(EXPENSE_FILE, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                amount, category, date = row
                expenses.append({
                    'amount': float(amount),  # Convert amount to float for calculations
                    'category': category,
                    'date': date
                })
    return expenses

# Function to view spending by category
def category_summary(expenses):
    """
    Sums up and displays total spending for each category.
    """
    category_totals = {}  # Dictionary to store total amounts per category
    for expense in expenses:
        category = expense['category']
        amount = expense['amount']
        if category in category_totals:
            category_totals[category] += amount  # Add amount to the existing category total
        else:
            category_totals[category] = amount  # Create a new category entry if it doesn't exist

    # Print the total spending per category
    print("\nTotal spending by category:")
    for category, total in category_totals.items():
        print(f"{category}: ${total:.2f}")
    print()

# Function to view total overall spending
def total_spending(expenses):
    """
    Calculates and displays the total spending across all categories.
    """
    total = sum(expense['amount'] for expense in expenses)  # Sum up all expenses
    print(f"\nTotal overall spending: ${total:.2f}\n")

# Function to view spending over time (by month)
def spending_over_time(expenses):
    """
    Groups expenses by month and displays total spending for each month.
    Optionally, creates a bar chart of monthly spending.
    """
    monthly_totals = {}  # Dictionary to store total spending per month
    
    for expense in expenses:
        date = expense['date'][:7]  # Extract the year and month from the date (YYYY-MM)
        amount = expense['amount']
        if date in monthly_totals:
            monthly_totals[date] += amount  # Add amount to the existing month's total
        else:
            monthly_totals[date] = amount  # Create a new month entry if it doesn't exist

    # Print the total spending per month
    print("\nSpending over time (monthly):")
    for month, total in monthly_totals.items():
        print(f"{month}: ${total:.2f}")
    
    # Plot the monthly spending summary using matplotlib
    plot_monthly_spending(monthly_totals)

# Function to create a bar chart of monthly spending
def plot_monthly_spending(monthly_totals):
    """
    Uses matplotlib to create and display a bar chart of monthly spending.
    """
    months = list(monthly_totals.keys())  # List of months
    totals = list(monthly_totals.values())  # Corresponding spending amounts
    
    plt.figure(figsize=(8, 5))  # Set figure size
    plt.bar(months, totals, color='skyblue')  # Create bar chart
    plt.xlabel('Month')  # X-axis label
    plt.ylabel('Total Spending ($)')  # Y-axis label
    plt.title('Monthly Spending Summary')  # Chart title
    plt.xticks(rotation=45)  # Rotate month labels for readability
    plt.tight_layout()  # Adjust layout for better appearance
    plt.show()  # Display the chart

# Function to delete an expense
def delete_expense():
    """
    Displays current expenses, allows the user to delete one by selecting from a list,
    and saves the updated list of expenses back to the CSV file.
    """
    expenses = load_expenses()  # Load existing expenses
    if not expenses:
        print("No expenses to delete.")
        return

    # Display a list of current expenses
    print("\nCurrent expenses:")
    for i, expense in enumerate(expenses):
        print(f"{i+1}. {expense['category']}, ${expense['amount']}, {expense['date']}")

    # User selects which expense to delete by index
    index = int(input("Enter the number of the expense to delete: ")) - 1
    if 0 <= index < len(expenses):  # Ensure valid index
        del expenses[index]  # Remove the selected expense
        save_expenses(expenses)  # Save the updated list of expenses
        print("Expense deleted successfully!\n")
    else:
        print("Invalid selection.\n")

# Function to save expenses back to the CSV file
def save_expenses(expenses):
    """
    Writes the current list of expenses to the CSV file, overwriting the previous data.
    """
    with open(EXPENSE_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        for expense in expenses:
            writer.writerow([expense['amount'], expense['category'], expense['date']])

# Main menu function
def main_menu():
    """
    Displays the main menu of the program, allowing the user to choose actions such as
    adding an expense, viewing summaries, deleting an expense, or exiting the program.
    The loop continues until the user chooses to exit.
    """
    while True:
        # Display menu options
        print("Personal Expense Tracker")
        print("1. Add an expense")
        print("2. View summaries")
        print("3. Delete an expense")
        print("4. Exit")
        
        choice = int(input("Enter your choice: "))  # Get user's choice

        # Call the corresponding function based on the choice
        if choice == 1:
            add_expense()  # Add a new expense
        elif choice == 2:
            view_summary()  # View expense summaries
        elif choice == 3:
            delete_expense()  # Delete an existing expense
        elif choice == 4:
            print("Exiting program. Goodbye!")
            break  # Exit the program
        else:
            print("Invalid choice. Please try again.")

# Run the program if this file is executed
if __name__ == '__main__':
    main_menu()


