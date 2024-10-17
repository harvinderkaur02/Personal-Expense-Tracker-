# Personal-Expense-Tracker-
The Personal Expense Tracker is a Python-based project designed to help users efficiently manage and track their daily spending. The application allows users to log expenses, categorize them, and view detailed summaries of their spending habits. key features include: 

# Key Features :
1. Add Expenses: Users can input expenses by specifying the amount, category (e.g., Food, Transport, Entertainment), and date (auto-generated if not provided).
2. View Summaries: Provides three types of summaries:
                            .  Total Spending by Category: Shows how much has been spent in each category.
                            .  Total Overall Spending: Displays the total amount spent.
                            .  Spending Over Time: Gives a monthly breakdown of expenses, visualized with charts.
3. Delete Expenses: Users can review and remove any incorrect or unnecessary entries.
4. Data Persistence: Expenses are saved to a CSV file, allowing data to be retrieved even after restarting the application.
   
# Bonus Feature:
Visualization: Monthly spending data is represented graphically using Matplotlib, helping users get a clear picture of their financial habits.

# Technologies Used:
            . Python for core logic and file handling
            . CSV module for data storage
            . Matplotlib for data visualization

This project is an excellent example of practical Python application, covering file handling, data structures, and basic data analysis, while offering a user-friendly interface.

# Explanation Of the Code:

1. Imports and File Setup:
   
    .  csv: This module is used to handle reading and writing expense data to a CSV file, ensuring persistence between program runs.
    .  datetime: Helps in managing dates, particularly for handling the current date.
    .  os: This module checks if the expense file exists before loading data.
    .  matplotlib.pyplot: Used for visualizing the spending data with plots (for the bonus feature).
    .  EXPENSE_FILE is the name of the file where all expense data will be saved. This file stores expense records in CSV format.

2. Function to Add Expenses :

   Purpose: This function takes user input for a new expense and saves it to the CSV file.
             . The user enters the amount, category, and date of the expense.
             . If the date is not provided, it defaults to today’s date.
             . The expense is appended (mode 'a') to the CSV file.
   
3. Function to View Summaries:

   Purpose: This function displays different types of summaries based on user input:
            a. First, it loads all existing expenses using the load_expenses() function.
            b. The user can choose between three types of summaries:
                                            .  Total spending by category.
                                            .  Total overall spending.
                                            .  Spending over time (monthly).
   
4. Loading Expenses from CSV:

   Purpose: This function loads expense data from the CSV file and returns it as a list of dictionaries.
                            .  Each expense is stored as a dictionary with keys: amount, category, and date.
                            .  If the file does not exist, an empty list is returned.

5. Category Summary:

   Purpose: This function calculates and displays the total spending per category.
                     . It iterates over the list of expenses and sums up the amounts for each category.
   
6. Total Overall Spending:

   Purpose: This function calculates the total spending across all categories and prints the result.
 
7. Spending Over Time (Monthly):

   Purpose: This function calculates the total spending for each month and prints the result. It also generates a plot of the monthly spending.
             . It extracts the year and month (YYYY-MM) from the date field to group expenses by month.
   
8. Plotting Monthly Spending:

   Purpose: This function creates a bar chart of monthly spending using matplotlib. The chart is shown to the user when the summary of spending over time is requested.
    
9. Delete an Expense:

   Purpose: This function allows the user to delete an expense by selecting from a list of current expenses. It deletes the chosen expense and updates the CSV file.
   
10 Saving Expenses to CSV:

   Purpose: This function saves the current list of expenses to the CSV file after an expense is deleted.
   
11. Main Menu:

    Purpose: This is the main user interface for the program. The menu offers the following options:
                        . Add an expense
                        . View summaries
                        . Delete an expense
                        . Exit the program
The while True loop ensures the menu keeps appearing until the user chooses to exit.

# Conclusion
This program gives the user a simple and intuitive way to log and track personal expenses. It uses CSV for data persistence, meaning that expenses are saved between runs. It also includes a visual element for viewing monthly spending trends using matplotlib.


    
