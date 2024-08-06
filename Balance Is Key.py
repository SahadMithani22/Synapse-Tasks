#Task 1.3
request_spending = {
"Mahek": {
    "balance": 3000.00,
    "transactions": [
    {"amount": -9000.00, "category": "Creatives"},
    {"amount": 7000.00, "category": "Sponsor"},
    {"amount": -2000.00, "category": "Prize-Money"}
]
},
"Arham": {
"balance": 5000.00,
"transactions": [
    {"amount": 8000.00, "category": "Stalls"},
    {"amount": 7500.00, "category": "Seminars"}
]
},

"Unnati": {
"balance": 3500.00,
"transactions": [
    {"amount": -5000.00, "category": "Attraction"},
    {"amount": 2500.00, "category": "Promo"},
    {"amount": -900.00, "category": "Lighting"},
    {"amount": 3000.00, "category": "Games"}
]
},

"Gaurang": {
"balance": 2000.00,
"transactions": [
    {"amount": 1500.00, "category": "Website"},
    {"amount": 1000.00, "category": "C2C"},
    {"amount": -500.00, "category": "Posters"}
]
}
}
def total_spending(request_spending, account_id:str, cat:str):
    spending_transactions = request_spending[account_id]['transactions']
    for i in spending_transactions:
        if(i['category'] == cat):
            return (i['amount'])
            continue
        

def account_balance(request_spending, account_id : str):
    sum = 0
    account_id_transactions = request_spending[account_id]['transactions']
    print(account_id_transactions) #Storing the 'transactions' dictionary in another dictionary named 'account_id_transactions'
    for i in account_id_transactions: #Iterating through the new dictionary
        sum = sum + i['amount']
    print(f'{request_spending[account_id]['balance'] + sum} is the remaining balance of {account_id} at the end of the event.')
    

def money_owed(request_spending, account_id):
    dictForOwed = request_spending[account_id]['transactions']
    sumOwed = 0
    for i in dictForOwed:
        sumOwed = sumOwed + i['amount']
    print(f'{((-1 * (request_spending[account_id]['balance'] + sumOwed)))} is the amount owed by the entered account.')


account_id = input('Enter the account ID:')
cat = input('Enter the category:')
print(total_spending(request_spending, account_id , cat))

#Output
# Enter the account ID:Gaurang
# Enter the category:Website
# 1500.0

account_id = input('Enter the account whose balance is required.')
(account_balance(request_spending, account_id))

#Output
# [{'amount': -5000.0, 'category': 'Attraction'}, 
# {'amount': 2500.0, 'category': 'Promo'}, 
# {'amount': -900.0, 'category': 'Lighting'}, 
# {'amount': 3000.0, 'category': 'Games'}]
# 3100.0 is the remaining balance of Unnati at the end of the event.

account_id = input('Enter the account ID for which the money owed is required.')
money_owed(request_spending, account_id)

#Output
# Enter the account ID for which the money owed is required.Unnati
# -3100.0 is the amount owed by the entered account.