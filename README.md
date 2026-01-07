# Expense Tracker (Python)

A simple **terminal-based Expense Tracker** built using Python fundamentals.
This project helps track daily expenses, view all expenses, and calculate the total amount spent.

---

## Features
- Add expenses
- View all expenses
- Show total expense
- Input validation (prevents crashes)
- Menu-driven terminal program

---

## Concepts Used
- Python dictionaries
- Loops (`while`, `for`)
- Conditional statements (`if-elif-else`)
- Functions
- String methods (`isdigit`, `lower`)
- Input validation

---

## How the Program Works
1. User selects an option from the menu.
2. Expenses are stored as **key-value pairs**:
   - Key → Expense name
   - Value → Amount
3. Duplicate expenses are handled by **adding to existing values**.
4. Invalid inputs are handled safely without crashing the program.

---

## How to Run the Program

1. Open terminal / command prompt
2. Navigate to the folder containing the file
3. Run the program:

```bash
python expense_tracker.py


```
## Example Menu
menu options:
1. add expense
2. view expense
3. show total
4. exit
```
```
## Example Output
coffee = 120
tea = 50
food = 300
the total expense is: 470
```
