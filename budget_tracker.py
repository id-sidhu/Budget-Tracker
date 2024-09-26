import numpy as np
import json
import os
import matplotlib.pyplot as plt
from datetime import datetime

def default_structure():
    return {
        "categories": ["Income", "Expenses", "Savings"],
        "transactions": {
            "Income": [],
            "Savings": [],
            "Expenses": {
                "Rent": [],
                "Groceries": [],
                "Transport": [],
                "Entertainment": []
            }
        }
    }

def load_data():
    if os.path.exists("budget_data.json"):
        with open('budget_data.json', 'r') as f:
            content = f.read().strip()
        if content:
            return json.loads(content)
        else:
            return default_structure()

    else:
        return default_structure()

data = load_data()
categories = data['categories']
income = data['transactions']['Income']
expenses = data['transactions']['Expenses']
savings = data['transactions']['Savings']
rent = data['transactions']['Expenses']['Rent']
groceries = data['transactions']['Expenses']['Groceries']
transport = data['transactions']['Expenses']['Transport']
entertainment = data['transactions']['Expenses']['Entertainment']

def totals():
    return {
    'Income': calc_total(income),
    'Savings': calc_total(savings),
    'Rent': calc_total(rent),
    'Groceries': calc_total(groceries),
    'Transport': calc_total(transport),
    'Entertainment': calc_total(entertainment)
    }
 
def save_data(data):
    with open('budget_data.json', 'w') as f2:
        json.dump(data, f2, indent=4)

def add_amount(array):
    amount_to_be_added = float(input("Enter total transaction amount ($): "))
    date_of_transaction = input("Enter the date of transaction (YYYY-MM-DD) or press enter for today's date: ")
    if date_of_transaction:
        transaction_date = date_of_transaction
    else:
        transaction_date = datetime.today().strftime('%Y-%m-%d')
    array.append({
        'amount': amount_to_be_added,
        'date': transaction_date
    })
    save_data(data)
    print(f'A transaction of {amount_to_be_added}$ added successfully!')
    return array

def delete_entry(arr, entry):
    if entry in arr:
        arr.remove(entry)
        save_data(data)
        print(f'Entry {entry} deleted successfully!')
    else:
        print(f'Entry {entry} not found in the list.')
    return arr

def add_category(array):
    category_to_be_added = input("Type the name of category you would like to add: ")
    array.append(category_to_be_added)
    save_data(data)
    print(f"{category_to_be_added} added successfully!")
    return array

def loop_entries(arr1):
    for index, category in enumerate(arr1):
        print(f"{index}. {category}")
    print(f"{len(arr1)}. Plot pie-chart summary")
    print(f"{len(arr1)+1}. Plot line-chart summary")
    print(f"{len(arr1)+2}. Add another category")
    print(f"{len(arr1)+3}. Delete entry")
    

def list_categories(arr1):
    for index, category in enumerate(arr1):
        print(f"{index}. {category}")

def calc_total(arr2):
    if isinstance(arr2, dict):
        sum_total = 0
        for category in arr2.values():
            for transaction in category:
                sum_total += float(transaction['amount'])
        return sum_total
    elif isinstance(arr2, list):
        sum_total = 0
        for x in arr2:
            sum_total += float(x['amount'])
        return sum_total
    else:
        print("Invalid input type for calculating total")
        return 0

def plot_pie():
    plt.figure()
    sizes = list(totals().values())
    labels = list(totals().keys())
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', textprops={'fontsize': 12})
    plt.title('Overall Distribution of Expenses and Income')
    plt.legend()
    plt.show()

def plot_line():
    plt.plot([datetime.strptime(trans['date'], '%Y-%m-%d') for trans in income], [trans['amount'] for trans in income], label='Income')
    plt.plot([datetime.strptime(trans['date'], '%Y-%m-%d') for trans in savings], [trans['amount'] for trans in savings], label='Savings')
    plt.plot([datetime.strptime(trans['date'], '%Y-%m-%d') for trans in groceries], [trans['amount'] for trans in groceries], label='Groceries')
    plt.plot([datetime.strptime(trans['date'], '%Y-%m-%d') for trans in rent], [trans['amount'] for trans in rent], label='Rent')
    plt.plot([datetime.strptime(trans['date'], '%Y-%m-%d') for trans in transport], [trans['amount'] for trans in transport], label='Transport')
    plt.plot([datetime.strptime(trans['date'], '%Y-%m-%d') for trans in entertainment], [trans['amount'] for trans in entertainment], label='Entertainment') 
    plt.title('Your monthly chart')
    plt.xlabel('Days')
    plt.ylabel('Value ($)')
    plt.legend()
    plt.show()


loop_entries(categories)
money_io = int(input('Welcome, what are you here for? '))

if money_io == categories.index('Income'):
    income = add_amount(income)
elif money_io == categories.index('Savings'):
    savings = add_amount(savings)
elif money_io == categories.index('Expenses'):
    print("In which category would you like to add?")
    loop_entries(list(expenses.keys()))
    category_chosen = int(input("Enter category: "))
    expense_keys = list(expenses.keys())
    if category_chosen < len(expense_keys):
        selected_category = expense_keys[category_chosen]
        expenses[selected_category] = add_amount(expenses[selected_category])
    else:
        print("Invalid category selected!")
elif money_io == len(categories):
    plot_pie()
elif money_io == len(categories)+1:
    plot_line()
elif money_io == len(categories)+2:
    categories = add_category(categories)
elif money_io == len(categories) + 3:
    print("From which category you would like to delete adn entry?")
    list_categories(categories)
    del_index = int(input("Choose category: "))
    if categories[del_index] == 'Income':
        list_categories(income)
        income = delete_entry(income, input("Chose entry to be deleted."))
    elif categories[del_index] == 'Savings':
        list_categories(savings)
        savings = delete_entry(savings, input("Chose entry to be deleted."))
    elif categories[del_index] == 'Expenses':
            print("In which subcategory would you like to delete?")
            list_categories(list(expenses.keys()))
            subcategory_chosen = int(input("Enter subcategory: "))
            expense_keys = list(expenses.keys())
            if subcategory_chosen < len(expense_keys):
                selected_category = expense_keys[subcategory_chosen]
                list_categories(expenses[selected_category])
                expenses[selected_category] = delete_entry(expenses[selected_category], expenses[selected_category][int(input("Choose an entry to delete: "))])
            else:
                print("Invalid subcategory selected!")
else:
    print('Invalid choice!')

data['transactions']['Income'] = income
data['transactions']['Savings'] = savings
data['transactions']['Expenses'] = expenses

save_data(data)

print('Total income: ', calc_total(income), '$')
print('Total savings: ', calc_total(savings), '$')
print('Total rent: ', calc_total(rent), '$')
print('Total groceries: ', calc_total(groceries), '$')
print('Total entertainment: ', calc_total(entertainment), '$')
print('Total transport: ', calc_total(transport), '$')
total_expenses = sum([calc_total(expenses[category]) for category in expenses])
print('Remaining balance: ', calc_total(income) - total_expenses)
