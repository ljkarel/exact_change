def exact_change(amount_paid, item_cost, currency):
    string_answer = f'The exact change for an item that costs ${item_cost} with an amount paid of {amount_paid} {currency} is'
    def change_pesos(amount_paid, item_cost):
        pass

    def change_yen(amount_paid, item_cost):
        pass

    
    

    def change_euros(amount_paid, item_cost):
        nonlocal string_answer
        dollars = round(((amount_paid * 1.08) - item_cost) * 100, 2)
        US_currencies = {
            '$100 bill': 10000,
            '$50 bill':5000,
            '$20 bill' :2000,
            '$10 bill':1000,
            '$5 bill': 500,
            '$1 bill': 100,
            'quarter':25,
            'dime':10,
            'penny':1
        }

        for key in US_currencies:

            if dollars / US_currencies[key] >= 1:
                amount = round(dollars//US_currencies[key])
                dollars -= amount * US_currencies[key]
                if amount > 1 and key != 'penny':

                    string_answer = string_answer + " " + f'{amount} ' + key + 's,'

                elif dollars < 1 and amount == 1:

                    string_answer = string_answer + " and " + f'{amount} ' + key + '.'

                elif dollars == 0 and key != 'penny':

                    string_answer = string_answer + " and " + f'{amount} ' + key + 's.'

                elif key == 'penny' and amount > 1:

                    string_answer = string_answer + " and " + f'{amount} ' + 'pennies.'

                else:
                    
                    string_answer = string_answer + " " + f'{amount} ' + key + ',' 
    
    if(currency == 'euros'):
        change_euros(amount_paid, item_cost)

    def change_ruble(amount_paid, item_cost):
        pass

    return string_answer

print(exact_change(100, 62.13, 'euros'))