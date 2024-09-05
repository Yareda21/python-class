class BudgetTracker:
    def __init__(self):
        self._income = 0
        self._expenses = 0

    @property
    def income(self):
        return self._income

    @income.setter
    def income(self, value):
        if value >= 0:
            self._income = value
        else:
            raise ValueError("Income must be a non-negative number.")

    @property
    def expenses(self):
        return self._expenses

    @expenses.setter
    def expenses(self, value):
        if value >= 0:
            self._expenses = value
        else:
            raise ValueError("Expenses must be a non-negative number.")

    @property
    def balance(self):
        return self._income - self._expenses

    def add_income(self, amount):
        if amount > 0:
            self._income += amount
        else:
            raise ValueError("Income amount must be positive.")

    def add_expense(self, amount):
        if amount > 0:
            self._expenses += amount
        else:
            raise ValueError("Expense amount must be positive.")
