# Application Documentation

## How to run
- Run `pip install -r requirements.txt` in the root directory to download the application dependencies.
- Run `python .\UcarOzgurFinalProject.py` in the root directory.

## Features & User Manual
This application consists of 2 different pages.
- **Income Expense Calculation Page**
    - Income section
        - Income Type Selection Box: Choose the type of income from the drop-down menu (Salary, Freelance, Rent, Side Job, Other).
        - Income Amount Input Field: Enter the amount for the income.
        - Add Income Button: Click to add the entered income to the list.
    - Expense Section
        - Expense Type Selection Box: Choose the type of expense from the drop-down menu (Rent/Mortgage, Utilities, Groceries, Transportation, Entertainment, Other).
        - Expense Amount Input Field: Enter the amount for the expense.
        - Add Expense Button: Click to add the entered expense to the list.
    - Calculate Button
        - Calculate Button: A button that takes user to the "Results" page.
        - Income Expense Tracker Icon: An icon to make the page more appealing.
- **Results Page**
    - Monthly Income: The total of all monthly incomes, displayed individually.
    - Yearly Income: The sum of all yearly incomes, calculated by grouping monthly incomes using dictionaries by type and multiplying the total by 12.
    - Monthly Expense: The total of all individual monthly expenses, displayed individually.
    - Yearly Expense: The sum of all yearly expenses, calculated by grouping monthly expenses using dictionaries by type and multiplying the total by 12.
    - Yearly Total: The net profit or loss (Yearly Income - Yearly Expense). The Yearly Total label is dynamically colored and displays an image based on your financial status:
        - Green: Positive balance (Net profit) - Displays a positive money image.
        - Red: Negative balance (Net loss) - Displays a negative money image.
        - Black: Neutral balance (Break-even) - Displays a neutral money image.
    - Exit Button: Exits the application
        - Note: If you click on the "X" button of the window, it clears the `incomes` and `expenses` arrays so that you can make more calculations without having to re-run the application.

## Example Usage
- Run the application by following the steps mentioned in the "How to run" section.
- Enter a monthly income by selecting an income type from the dropdown and entering an income amount.
    - Income amount only accepts decimal numbers (integer or float), and if the user tries to enter something else they receive an error message. 
- A green message will be displayed at the bottom indicating that a new income has been successfully added. 
- Click "Add Income."
- Input fields will be cleared after entering an income, letting the user enter a new income.
- Enter a monthly expense by selecting an expense type from the dropdown and entering an expense amount.
    - Expense amount only accepts decimal numbers (integer or float), and if the user tries to enter something else they receive an error message. 
- A red message will be displayed at the bottom indicating that a new expense is successfully added. 
- Click "Add Expense."
- Input fields will be cleared after entering an expense, letting the user enter a new expense.
- Click the "Calculate" button to view detailed financial results, this action will take you to the "Results" page.
- Here on this page, you can review all your monthly and yearly incomes and expenses. 
    - Monthly incomes and monthly expenses are displayed individually with their expense types and expense amounts. The total of these amounts is also displayed at the top of their section.
    - Yearly incomes and yearly expenses are displayed by grouping monthly incomes and expenses respectively and multiplying the total by 12. 
    - Yearly Total: The net profit or loss (Yearly Income - Yearly Expense). The Yearly Total label is dynamically colored and displays an image based on your financial status.
- You can use the Exit button at the bottom of this page to close the application altogether, or you can click on the "X" button of the "Results" window to close the "Results" page and start making another income & expense calculation. Clicking on the "X" on the "Results" page clears the `incomes` and `expenses` arrays.

## Images (PNGS) I used in this application
<img src="./images/expense.png" alt="expense" width="50" height="50"/>
<img src="./images/negative_money.png" alt="negative money" width="50" height="50"/>
<img src="./images/neutral_money.png" alt="neutral money" width="50" height="50"/>
<img src="./images/positive_money.png" alt="positive money" width="50" height="50"/>