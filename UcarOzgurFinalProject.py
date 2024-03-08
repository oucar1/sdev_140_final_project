# Ozgur Ucar - C06566469
# M08 Final Project

"""
This Python program is a financial management tool designed for users to easily track their income and expenses. 
It allows for the input of income and expense types and amounts. The program maintains separate lists for income and expenses, 
and upon clicking the "Calculate" button, it opens a window displaying monthly and yearly totals, net profit or loss, and yearly totals categorized by types. 
The result window uses colored labels and visuals to represent the financial status, providing a quick overview. 
Additionally, the program ensures a clean start for each tracking period by clearing the lists when the result window is closed.
"""


import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk


class IncomeExpenseTracker:
    def __init__(self, master):
        self.master = master
        
        # Setting the title of the window
        self.master.title("Income Expense Tracker")
        # Image that we will be using in the form
        self.expense_image = ImageTk.PhotoImage(Image.open("./images/expense.png").resize((50, 50)))

        # Arrays to store all the incomes and expenses in the application
        self.incomes = []
        self.expenses = []

        # Setting up the Income and Expense sections
        self.setup_income_section()
        self.setup_expense_section()

        # Button that triggers a new window to display the monthly and yearly totals, as well as the net profit/loss
        self.button_calculate = ttk.Button(master, text="Calculate", command=self.calculate_totals)

        # Message label for displaying success messages
        self.message_label = ttk.Label(master, text="", foreground="green")
        self.message_label.configure(image=self.expense_image, compound="top")

        # Center the main form window on the screen
        self.center_window(self.master, 400, 400, True)

        # Set a fixed size for the main window
        # self.master.geometry("400x400")

        # Arranging the Calculate button and message label for displaying success messages
        self.button_calculate.grid(row=6, column=0, columnspan=2, pady=5)
        self.message_label.grid(row=7, column=0, columnspan=2, pady=5)

        # Centering the labels, comboboxes, and buttons horizontally
        # Weight arguments make the columns equally expandable if applicable (if the window is resizable)
        # This window is not resizable but I'm still using them since it makes it easier to center them horizontally
        self.master.columnconfigure(0, weight=1)
        self.master.columnconfigure(1, weight=1)

    ### Centers the passed in window on the screen
    ### isFixed argument is used to set the window to be resizable or not
    def center_window(self, window, width, height, isFixed=False):

        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x_position = (screen_width - width) // 2
        y_position = (screen_height - height) // 2

        if isFixed:
            window.resizable(False, False)  
        else:
            window.resizable(True, True) 
            
        ## Initialize the windows at the center of the screen.
        window.geometry(f"{width}x{height}+{x_position}+{y_position}")

    ### Displays the message after a new expense or income is added to their corresponding lists
    ### Message is cleared after 1500 milliseconds  = 1.5 seconds
    def show_message(self, message, color="green"):
        # Color is green by default but for expenses, the text color is red
        self.message_label.config(text=message, foreground=color)
        self.master.after(1500, lambda: self.message_label.config(text="", foreground="green"))

    ### Setting up the Income section's labels, comboboxes, and buttons
    def setup_income_section(self):
        self.label_income_type = ttk.Label(self.master, text="Income Type:")
        self.income_type_var = tk.StringVar()
        self.income_types_combobox = ttk.Combobox(self.master, textvariable=self.income_type_var,
                                                  values=["Salary", "Freelance", "Rent", "Side Job", "Other"])

        self.label_income_amount = ttk.Label(self.master, text="Income Amount:")
        self.entry_income_amount = ttk.Entry(self.master)

        self.button_income_add = ttk.Button(self.master, text="Add Income", command=self.add_income)

        self.arrange_income_section()

    ### Setting up the user interface layout for the income section 
    ### Seperated the layout from the setup method makes the code more readable
    def arrange_income_section(self):
        self.label_income_type.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.income_types_combobox.grid(row=0, column=1, padx=10, pady=5)
        self.label_income_amount.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry_income_amount.grid(row=1, column=1, padx=10, pady=5)
        self.button_income_add.grid(row=2, column=0, columnspan=2, pady=10)

    ### Setting up the Expense section's labels, comboboxes, and buttons
    def setup_expense_section(self):
        self.label_expense_type = ttk.Label(self.master, text="Expense Type:")
        self.expense_type_var = tk.StringVar()
        self.expense_types_combobox = ttk.Combobox(self.master, textvariable=self.expense_type_var,
                                                   values=["Rent/Mortgage", "Utilities", "Groceries", "Transportation", "Entertainment", "Other"])

        self.label_expense_amount = ttk.Label(self.master, text="Expense Amount:")
        self.entry_expense_amount = ttk.Entry(self.master)

        self.button_expense_add = ttk.Button(self.master, text="Add Expense", command=self.add_expense)

        self.arrange_expense_section()

    ### Setting up the user interface layout for the expense section
    ### Seperated the layout from the setup method makes the code more readable
    def arrange_expense_section(self):
        self.label_expense_type.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.expense_types_combobox.grid(row=3, column=1, padx=10, pady=5)
        self.label_expense_amount.grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.entry_expense_amount.grid(row=4, column=1, padx=10, pady=5)
        self.button_expense_add.grid(row=5, column=0, columnspan=2, pady=10)

    ### Method to add a new income to the list
    def add_income(self):
        income_type = self.income_type_var.get()
        income_amount = self.entry_income_amount.get()

        # Checking if the user has entered both the income type and amount
        # if not, an error message in a pop-up is displayed
        if not income_type or not income_amount:
            messagebox.showerror("Error", "Please fill in all income fields.")
            return

        # Checking if the user has entered a valid number for the income amount (only accepting decimal numbers)
        # if not, an error message in a pop-up is displayed
        try:
            income_amount = float(income_amount)
        except ValueError:
            messagebox.showerror("Error", "Invalid income amount. Please enter a number.")
            return

        # If the user has succesfully entered both the income type and amount, the income is added to the list
        # Add income to the list
        self.incomes.append({"Income Type": income_type, "Amount": income_amount})

        # Show success message in green (green means it's an income)
        self.show_message(f"{income_type} income for ${income_amount:.2f} added to incomes")

        # Clear input fields so that the user can enter a new income
        self.income_type_var.set("")
        self.entry_income_amount.delete(0, tk.END)

    ### Method to add a new expense to the list
    def add_expense(self):
        expense_type = self.expense_type_var.get()
        expense_amount = self.entry_expense_amount.get()

        # Checking if the user has entered both the expense type and amount
        if not expense_type or not expense_amount:
            messagebox.showerror("Error", "Please fill in all expense fields.")
            return

        # Checking if the user has entered a valid number for the expense amount (only accepting decimal numbers)
        # if not, an error message in a pop-up is displayed
        try:
            expense_amount = float(expense_amount)
        except ValueError:
            messagebox.showerror("Error", "Invalid expense amount. Please enter a number.")
            return

        # If the user has succesfully entered both the expense type and amount, the expense is added to the list
        # Add expense to the list
        self.expenses.append({"Expense Type": expense_type, "Amount": expense_amount})

        # Show success message in red (red means it's an expense)
        self.show_message(f"{expense_type} expense for ${expense_amount:.2f} added to expenses", color="red")

        # Clear input fields so that the user can enter a new expense
        self.expense_type_var.set("")
        self.entry_expense_amount.delete(0, tk.END)
        
    ### Method to display the monthly and yearly totals for incomes and expenses
    def display_totals(self, window, label_text, total_amount, items, color):
        # Display the monthly total for incomes or expenses
        ttk.Label(window, text=f"{label_text}: ${total_amount:.2f}", foreground=color).pack(pady=5)
        
        # Iterate through all the items in the array (income or expense) and a new TKinter label is created for each item
        for item in items:
            # If the label text contains "Income", then the item type is set to the income type, otherwise it's set to the expense type
            item_type = item['Income Type'] if 'Income' in label_text else item['Expense Type']
            amount = item['Amount']
            formatted_text = f"{item_type}: ${amount:.2f}"

            # label_pack() is used to display the label in the window
            label = ttk.Label(window, text=formatted_text).pack(pady=5)
            # label.pack()
            
        ttk.Separator(window, orient="horizontal").pack(fill="x", pady=10)

    ### Method to display the yearly totals for incomes and expenses
    def display_yearly_totals(self, window, label_text, total_amount, items, color):
        ttk.Label(window, text=f"{label_text}: ${total_amount:.2f}", foreground=color).pack(pady=5)
        yearly_dict = {}
        
        # Similar to the display_totals method, we iterate through all the items in the array (income or expense)
        # and a new TKinter label is created for each item
        # The difference here is that we are grouping the items by their type and calculating the total amount for each type using a dictionary
        for item in items:
            type_name = item['Income Type'] if 'Income' in label_text else item['Expense Type']
            yearly_dict.setdefault(type_name, [])
            yearly_dict[type_name].append(item['Amount'])
        for type_name, amounts in yearly_dict.items():
            total_amount = sum(amounts) * 12
            ttk.Label(window, text=f"{type_name}: ${total_amount:.2f}").pack(pady=5)
            
        ttk.Separator(window, orient="horizontal").pack(fill="x", pady=10)

    ### Method to color the total label and set the image based on the balance
    def color_total_label(self, label, amount):
        # If positive balance (net profit) --> set the label color to green and display the positive money image
        # If negative balance (net loss) ->> set the label color to red and display the negative money image
        # If the balance is 0 --> set the label color to black and display the neutral money image
        if amount > 0:
            label.configure(foreground="green", image=self.positive_money_image, compound="bottom")
        elif amount < 0:
            label.configure(foreground="red", image=self.negative_money_image, compound="bottom")
        else:
            label.configure(image=self.neutral_money_image, compound="bottom")

    ### Method to calculate the monthly and yearly totals for incomes and expenses
    ### Also calculates the net profit/loss and displays the results in a new window
    def calculate_totals(self):
        # Check if both income and expense lists are empty - if so, display an error message in a pop-up
        if not self.incomes and not self.expenses:
            messagebox.showerror("Error", "Please add incomes OR expenses before calculating.")
            return

        # Images that we will be using conditionally to display at the bottom of the page
        self.positive_money_image = ImageTk.PhotoImage(Image.open("./images/positive_money.png").resize((50, 50)))
        self.negative_money_image = ImageTk.PhotoImage(Image.open("./images/negative_money.png").resize((50, 50)))
        self.neutral_money_image = ImageTk.PhotoImage(Image.open("./images/neutral_money.png").resize((50, 50)))

        # Iterating through the incomes list to calculate the monthly income total
        monthly_income_total = 0
        for item in self.incomes:
            monthly_income_total += item['Amount']

        # Iterating through the expenses list to calculate the monthly expense total
        monthly_expense_total = 0
        for item in self.expenses:
            monthly_expense_total += item['Amount']
        
        # Annual income and expense total is basically calculated by multiplying the monthly totals by 12
        annual_income_total = monthly_income_total * 12
        annual_expense_total = monthly_expense_total * 12
        
        # Net profit or loss is calculated by subtracting the annual expense total from the annual income total
        net_profit_loss = annual_income_total - annual_expense_total

        # Create a new window and center it on the screen
        result_window = tk.Toplevel(self.master)
        result_window.title("Results")
        self.center_window(result_window, 400, 600, False)

        # Monthly Incomes
        self.display_totals(result_window, "Monthly Income", monthly_income_total, self.incomes, "green")

        # Yearly Income (Monthly Incomes * 12)
        self.display_yearly_totals(result_window, "Yearly Income", annual_income_total, self.incomes, "green")

        # Monthly Expenses
        self.display_totals(result_window, "Monthly Expense", monthly_expense_total, self.expenses, "red")

        # Yearly Expense (Monthly Expenses * 12)
        self.display_yearly_totals(result_window, "Yearly Expense", annual_expense_total, self.expenses, "red")

        # Total label
        total_label = ttk.Label(result_window, text=f"Yearly Total: ${net_profit_loss:.2f}")
        total_label.pack(pady=5)

        # Color the total label and set the image based on the balance
        self.color_total_label(total_label, net_profit_loss)
        
        # Add an Exit button to close both the result window and the main application window
        exit_button = ttk.Button(result_window, text="Exit", command=lambda: self.exit_application(result_window))
        exit_button.pack(pady=10)
        
        # https://stackoverflow.com/questions/20039096/tkinter-check-if-root-has-been-destroyed
        result_window.protocol("WM_DELETE_WINDOW", lambda: self.on_result_window_close(result_window))

    ### Method to clear the incomes and expenses arrays when the result window is closed
    def on_result_window_close(self, window):
        # Clear the incomes and expenses arrays
        self.incomes = []
        self.expenses = []
        print(f"Incomes: {self.incomes}, Expenses: {self.expenses}")

        window.destroy()
        
    # Method to exit from the entire application
    def exit_application(self, window):
        window.destroy()  # 
        self.master.destroy()  


if __name__ == "__main__":
    root = tk.Tk()
    app = IncomeExpenseTracker(root)
    root.mainloop()
