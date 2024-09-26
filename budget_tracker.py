import numpy as np
import json
import os
import matplotlib.pyplot as plt

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

    
def save_data(data):
    f2 = open('budget_data.json', 'w')
    json.dump(data, f2, indent = 4)
    f2.close()

def add_amount(array):
    amount_to_be_added = float(input("Enter total transaction amount ($): "))
    array.append(amount_to_be_added)
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
    array.insert((len(array)-1), category_to_be_added)
    save_data(data)
    print(f"{category_to_be_added} added successfully!")
    return array

def loop_entries(arr1):
    for index, category in enumerate(arr1):
        print(f"{index}. {category}")
    return None

def total(arr2):
    sum = 0
    for x in arr2:
        sum = sum + x
    return sum

data = load_data()
categories = data['categories']
income = data['transactions']['Income']
expenses = data['transactions']['Expenses']
savings = data['transactions']['Savings']
rent = data['transactions']['Expenses']['Rent']
groceries = data['transactions']['Expenses']['Groceries']
transport = data['transactions']['Expenses']['Transport']
entertainment = data['transactions']['Expenses']['Entertainment']
days = list(range(1,32))

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
elif money_io < len(categories):
    categories = add_category(categories)
else:
    print('Invalid choice!')

data['transactions']['Income'] = income
data['transactions']['Savings'] = savings
data['transactions']['Expenses'] = expenses

save_data(data)

print('Total income: ', total(income), '$')
print('Total savings: ', total(savings), '$')
print('Total rent: ', total(rent), '$')
print('Total groceries: ', total(groceries), '$')
print('Total entertainment: ', total(entertainment), '$')
print('Total transport: ', total(transport), '$')

plt.plot(range(len(income)), income, label='Income')  
plt.plot(range(len(savings)), savings, label='Savings') 
plt.plot(range(len(groceries)), groceries, label='Groceries') 
plt.plot(range(len(rent)), rent, label='Rent')  
plt.plot(range(len(transport)), transport, label='Transport') 
plt.plot(range(len(entertainment)), entertainment, label='Entertainment') 
plt.title('Your monthly chart')
plt.xlabel('Days')
plt.ylabel('Value ($)')
plt.legend()
plt.show()