amount_due = 50
while amount_due > 0:
    print(f'Amount Due: {amount_due}')
    coin = int(input('Insert Coin: '))
    if coin in [25, 10, 5]:
        amount_due -= coin
    if amount_due < 0:
        change_owed = abs(amount_due)
        print(f'Change Owed: {change_owed}')
        break
if amount_due == 0:
    print(f'Change Owed: 0')
    