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
    print("In which category would you like to add.")
    loop_entries(expenses)
    category_chosen = int(input("Enter category: "))
    if category_chosen == expenses.index("Add another category"):
        expenses = add_category(expenses)
    else:
        if category_chosen == expenses.index("Rent"):
           rent = add_amount(rent)
        elif category_chosen == expenses.index("Groceries"):
            groceries = add_amount(groceries)
        elif category_chosen == expenses.index("Transport"):
            transport = add_amount(transport)
        elif category_chosen == expenses.index("Entertainment"):
            entertainment = add_amount(entertainment)
elif money_io == categories.index('Add another category'):
    categories = add_category(categories)
elif money_io == categories.index('Remove entry'):
    catg = int(input('Enter category number from which you want to delete: '))
    catg_selected = categories[catg].lower()
    if catg_selected == 'income':
        print(f"Current entries in Income: {income}")
        entry_to_be_deleted = float(input('Enter transaction that you want to delete: '))
        income = delete_entry(income, entry_to_be_deleted)
    elif catg_selected == 'savings':
        print(f"Current entries in Savings: {savings}")
        entry_to_be_deleted = float(input('Enter transaction that you want to delete: '))
        savings = delete_entry(savings, entry_to_be_deleted)
    elif catg_selected == 'expenses':
        loop_entries(expenses)
        exp_catg = int(input('In which category in epenses would you like to delete: '))
        if exp_catg == expenses.index('Groceries'):
            print(f"Current entries in Groceries: {groceries}")
            entry_to_be_deleted = float(input('Enter transaction that you want to delete: '))
            groceries = delete_entry(groceries, entry_to_be_deleted)
        elif exp_catg == expenses.index('Rent'):
            print(f"Current entries in rent: {rent}")
            entry_to_be_deleted = float(input('Enter transaction that you want to delete: '))
            rent = delete_entry(rent, entry_to_be_deleted)
        elif exp_catg == expenses.index('Transport'):
            print(f"Current entries in Transport: {transport}")
            entry_to_be_deleted = float(input('Enter transaction that you want to delete: '))
            transport = delete_entry(transport, entry_to_be_deleted)
        elif exp_catg == expenses.index('Entertainment'):
            print(f"Current entries in Entertainment: {entertainment}")
            entry_to_be_deleted = float(input('Enter transaction that you want to delete: '))
            entertainment = delete_entry(entertainment, entry_to_be_deleted)
        else:
            print("Invalid category selected!")
else:
    print('Invalid choice!')

data['income'] = income
data['savings'] = savings
data['rent'] = rent
data['groceries'] = groceries
data['transport'] = transport
data['entertainment'] = entertainment
data['categories'] = categories
data['expenses'] = expenses

save_data(data)

print('Total income: ', total(income), '$')
print('Total savings: ', total(savings), '$')
print('Total rent: ', total(rent), '$')
print('Total groceries: ', total(groceries), '$')
print('Total entertainment: ', total(entertainment), '$')
print('Total transport: ', total(transport), '$')


plt.plot(income, label='Income')  
plt.plot(savings, label='Savings') 
plt.plot(groceries, label='Groceries') 
plt.plot(rent, label='Rent')  
plt.plot(transport, label='Transport') 
plt.plot(entertainment, label='Entertainment') 
plt.title('Your monthly chart')
plt.xlabel('Days')
plt.ylabel('Value')
plt.legend()
plt.show()