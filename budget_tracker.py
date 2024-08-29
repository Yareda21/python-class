class BudgetTracker:
    def __init__(self, initial_budget):
        self.budget = initial_budget
        self.expenses = []

    def add_expense(self, amount, description):
        if amount > self.budget:
            print("Expense exceeds available budget!")
        else:
            self.expenses.append({"amount": amount, "description": description})
            self.budget -= amount
            print(f"Added expense: {description} (${amount:.2f})")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
            return
        print("Expenses:")
        for expense in self.expenses:
            print(f"- {expense['description']}: ${expense['amount']:.2f}")

    def view_budget(self):
        print(f"Remaining budget: ${self.budget:.2f}")

def main():
    initial_budget = float(input("Enter your initial budget: "))
    tracker = BudgetTracker(initial_budget)

    while True:
        print("\nOptions:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Remaining Budget")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Enter expense amount: "))
            description = input("Enter expense description: ")
            tracker.add_expense(amount, description)
        elif choice == "2":
            tracker.view_expenses()
        elif choice == "3":
            tracker.view_budget()
        elif choice == "4":
            print("Exiting budget tracker.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()