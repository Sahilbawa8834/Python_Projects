expenses = []
def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})
#fn to print expenses
def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')
#fn to show total expenses
def total_expenses(expenses):
	return sum(expenses['amount'] for expense in expenses)
#filter expense by category
def filter_expenses_by_category(expenses, category):
    return [expense for expense in expenses if expense['category'] == category]
# Main function to run the program
def main():
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
        choice = input('Enter your choice: ')

        if choice == '1':
            try:
                amount = float(input('Enter amount: '))
                category = input('Enter category: ')
                add_expense(expenses, amount, category)
                print('Expense added successfully!')
            except ValueError:
                print('Invalid amount. Please enter a numeric value.')
        elif choice == '2':
            print('\nAll Expenses:')
            if expenses:
                print_expenses(expenses)
            else:
                print('No expenses recorded yet.')
        elif choice == '3':
            print('\nTotal Expenses:', total_expenses(expenses))
        elif choice == '4':
            category = input('Enter category to filter: ')
            filtered = filter_expenses_by_category(expenses, category)
            print(f'\nExpenses for category "{category}":')
            if filtered:
                print_expenses(filtered)
            else:
                print('No expenses found for this category.')
        elif choice == '5':
            print('Exiting the program. Goodbye!')
            break
        else:
            print('Invalid choice. Please try again.')

# Run the program
if __name__ == '__main__':
    main()




