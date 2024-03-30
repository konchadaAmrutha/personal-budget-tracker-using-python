from budget import Expense
import calendar
import datetime

def main():
    print("Running Expense Tracker")
    expense_file_path = "expenses.csv"
    Budget = 2000


    # getting input from user for expense
    budget = get_user_expense()

    #write their expense into a file
    save_to_file(budget,expense_file_path)

    #read file and summerize expense
    summerize_expense(expense_file_path,Budget)



def get_user_expense():
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))
    print()
    expense_categories = [
        " Food",
        " Home", 
        " Work",
        " Fun",
        " other",
    ]

    while True:
        print()
        print("select a category:")
        for i,category_name in enumerate(expense_categories):
            print(f"{i+1}. {category_name}")
        
        value_range=f"[1-{len(expense_categories)}]"

        try:
            selected_index = int(input(f"Enter a category number {value_range} :"))-1
            
            if selected_index in range(len(expense_categories)):

                selected_category = expense_categories[selected_index]
                new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount )
                return new_expense

            else:
                print("Invalid category number. Please try again!")
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")


        
    


def save_to_file(budget:Expense, expense_file_path):
    print(f"Saving user expense:{budget} to {expense_file_path}")
    with open (expense_file_path, "a") as f:          # "a" to add items in csv file 
        f.write(f"{budget.name},{budget.amount},{budget.category}\n")


def summerize_expense(expense_file_path,Budget):
    print()
    print("Summerize user expense")
    expenses:list[Expense]=[]
    with open(expense_file_path,"r") as f:
        lines=f.readlines()
        for line in lines:
            if not line.strip():
                continue
            parts = line.strip().split(",")
            expense_name, expense_amount, expense_category =parts
            line_expense=Expense(name=expense_name, amount=float(expense_amount), category=expense_category)
            expenses.append(line_expense)
    
    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount

    print("Expenses By category:")
    for key, amount in amount_by_category.items():
        print(f"  {key}: ₹{amount:.2f}")

    
    total_spent = sum([x.amount for x in expenses])
    print(f" Total Spent: ₹{total_spent:.2f}")

    remaining_budget = Budget - total_spent
    print()
    print(f"Budget Remaining: ₹{remaining_budget:.2f}")

    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day

    daily_budget = remaining_budget / remaining_days
    print()
    print(green(f"Budget Per Day: ₹{daily_budget:.2f}"))


def green(text):
    return f"\033[92m{text}\033[0m"


if __name__ == "__main__":
    main()