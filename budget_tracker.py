import numpy as np
import json
import os
import matplotlib.pyplot as plt
from datetime import datetime
import sys

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

def add_amount(category_name, category_list):
    if not budget_alert(category_name, category_list):
        return category_list
    
    try: 
        amount_to_be_added = float(input("Enter total transaction amount ($): "))
    except ValueError:
        print("Something went wrong. Make sure you have entered amount correctly.")
        return category_list

    try:    
        date_of_transaction = input("Enter the date of transaction (YYYY-MM-DD) or press enter for today's date: ")
        if date_of_transaction:
            transaction_date = date_of_transaction
        else:
            transaction_date = datetime.today().strftime('%Y-%m-%d')
    except ValueError:
        print("Something went wrong. Make sure you have entered amount correctly.")
        return category_list
    
    category_list.append({
        'amount': amount_to_be_added,
        'date': transaction_date
    })
    save_data(data)
    print(f'A transaction of {amount_to_be_added}$ added successfully!')
    return category_list

def delete_entry(arr, entry):
    try:
        found = next(item for item in arr if item.get('amount') == entry.get('amount') and item.get('date') == entry.get('date'))
        if found:
            arr.remove(found)
            save_data(data)
            print(f'Entry with amount {entry.get("amount")} and date {entry.get("date")} deleted successfully!')
        else:
            print('Entry not found in the list.')
    except Exception as e:
        print(f"An error occurred: {str(e)}")
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
                sum_total = sum_total + float(transaction['amount'])
        return sum_total
    elif isinstance(arr2, list):
        sum_total = 0
        for x in arr2:
            if 'amount' in x:  
                sum_total += float(x['amount'])
        return sum_total
    else:
        print("Invalid input type for calculating total")
        return 0

def plot_pie():
    plt.figure(figsize=(20,16))
    sizes = list(totals().values())
    labels = list(totals().keys())
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', textprops={'fontsize': 24})
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
    plt.xticks(rotation=45)
    plt.legend()
    plt.show()

def set_budget(bud_categ, bud):
    if bud_categ in expenses:
        expenses[bud_categ].append({"budget": bud})
        save_data(data)
        return f"Budget of {bud}$ is set successfully to {bud_categ}"
    else:
        print("Invalid category name.")

def budget_alert(category_name, category_transactions):
    budget_entry = None
    for entry in category_transactions:
        if 'budget' in entry:
            budget_entry = entry
            break

    if budget_entry:
        budget_limit = budget_entry['budget']
        current_total = calc_total(category_transactions)
        
        if current_total >= budget_limit:
            print(f"You have reached or exceeded your budget limit for {category_name}. Current total: ${current_total}, Budget: ${budget_limit}")
            proceed = input("Do you still want to add another transaction? (y/n): ").strip().lower()
            if proceed != 'y':
                print("Transaction cancelled to stay within the budget.")
                return False
    return True

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def main():
    global categories, income, expenses, savings, rent, groceries, transport, entertainment
    while True: 
        loop_entries(categories)
        money_io = input('Type (q) to quit or (s) to set budget limit for expenses.\nChoose a category: ')

        if money_io == 'q':  
            print("Bye Bye..")
            break  

        if money_io.isdigit():
            money_io = int(money_io)

        if money_io == categories.index('Income'):
            income = add_amount('Income', income)
        elif money_io == categories.index('Savings'):
            savings = add_amount('Savings', savings)
        elif money_io == categories.index('Expenses'):
            print("In which category would you like to add?")
            list_categories(list(expenses.keys()))
            category_chosen = int(input("Enter category: "))
            expense_keys = list(expenses.keys())
            if category_chosen < len(expense_keys):
                selected_category = expense_keys[category_chosen]
                expenses[selected_category] = add_amount(selected_category, expenses[selected_category])
            else:
                print("Invalid category selected!")
        elif money_io == len(categories):
            plot_pie()
        elif money_io == len(categories)+1:
            plot_line()
        elif money_io == len(categories)+2:
            categories = add_category(categories)
        elif money_io == len(categories) + 3:
            print("From which category you would like to delete an entry?")
            list_categories(categories)
            del_index = int(input("Choose category: "))
            if categories[del_index] == 'Income':
                list_categories(income)
                income = delete_entry(income, input("Choose entry to be deleted."))
            elif categories[del_index] == 'Savings':
                list_categories(savings)
                savings = delete_entry(savings, input("Choose entry to be deleted."))
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
        elif money_io == "s":
            list_categories(expenses)
            chose_categ = int(input("Choose category you want to set limit to: "))
            expenses_list = list(expenses.keys())
            chosen_categ = expenses_list[chose_categ]
            budget = float(input("Enter your budget here: "))
            print(set_budget(chosen_categ, budget))
        else:
            print('Invalid choice!')

        save_data(data)

        # print('Total income: ', calc_total(income), '$')
        # print('Total savings: ', calc_total(savings), '$')
        # print('Total rent: ', calc_total(rent), '$')
        # print('Total groceries: ', calc_total(groceries), '$')
        # print('Total entertainment: ', calc_total(entertainment), '$')
        # print('Total transport: ', calc_total(transport), '$')
        total_expenses = sum([calc_total(expenses[category]) for category in expenses])
        print('Remaining balance: ', calc_total(income) - total_expenses)
        loop_continuity = input("Do you want to make any other modification (y/n): ")
        if loop_continuity != 'y':
            clear_terminal()
            return False
        
        clear_terminal()


if __name__ == '__main__':
    main()
