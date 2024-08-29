class BudgetTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category):
        self.expenses.append({'amount': amount, 'category': category})
        print(f"Added expense: ${amount} for {category}")

    def total_expenses(self):
        return sum(expense['amount'] for expense in self.expenses)

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
            return
        print("Expenses:")
        for expense in self.expenses:
            print(f"Category: {expense['category']}, Amount: ${expense['amount']:.2f}")
        print(f"Total Expenses: ${self.total_expenses():.2f}")


def main():
    tracker = BudgetTracker()
    
    while True:
        print("\nBudget Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            amount = float(input("Enter the amount: "))
            category = input("Enter the category: ")
            tracker.add_expense(amount, category)
        elif choice == '2':
            tracker.view_expenses()
        elif choice == '3':
            print("Exiting the budget tracker.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()