def exact_change(amount_paid, item_cost):
    change = float(amount_paid - item_cost)

    if change < 0:
        return 'Your money is no good here.'
    
    change_dict = {
        '100':0,
        '50':0,
        '20':0,
        '10':0,
        '5':0,
        '1':0,
        '0.25':0,
        '0.10':0,
        '0.05':0,
        '0.01':0
    }
    last_value = ''
    for money in change_dict:
        while float(change) >= float(money):
            change = round(change, 2)
            change -= float(money) 
            change_dict[money] += 1
            if change == 0:
                last_value = money

    

    #print change
    print_state = f'The exact change for an item that costs ${item_cost} with an amount paid of ${amount_paid} is '

    for key, value in change_dict.items():
    
        if value > 1:
            if float(key) >= 1:
                print_state += f' {value} ${key} bills,'
            elif float(key) == float(last_value):
                if key == '0.25':
                    print_state += f' and {value} quarters.'
                elif key == '0.10':
                    print_state += f' and {value} dimes.'
                elif key == '0.05':
                    print_state += f' and {value} nickels.'
                elif key == '0.01':
                    print_state += f' and {value} pennies.'
            else:
                if key == '0.25':
                    print_state += f' {value} quarters,'
                elif key == '0.10':
                    print_state += f' {value} dimes,'
                elif key == '0.05':
                    print_state += f' {value} nickels,'
                elif key == '0.01':
                    print_state += f' {value} pennies,'
        elif value == 1:
            if float(key) > 1:
                print_state += f' {value} ${key} bill,'
            elif float(key) == float(last_value):
                if key == '0.25':
                    print_state += f' and {value} quarter.'
                elif key == '0.10':
                    print_state += f' and {value} dime.'
                elif key == '0.05':
                    print_state += f' and {value} nickel.'
                elif key == '0.01':
                    print_state += f' and {value} penny.'
            else:
                if key == '0.25':
                    print_state += f' {value} quarter,'
                elif key == '0.10':
                    print_state += f' {value} dime,'
                elif key == '0.05':
                    print_state += f' {value} nickel,'
                elif key == '0.01':
                    print_state += f' {value} penny,'
    
    # split_str = print_state.split(',')
    # last_elem = split_str[-1]
    # del split_str[-1]
    # split_str.append(' and ' + last_elem)
    # split_str.append('.')
    
    # new_str = ",".join(split_str)
    # print(new_str)
            
        
        

    return print_state
    def change_pesos(amount_paid, item_cost):
        pass

    def change_yen(amount_paid, item_cost):
        #convert to US dollars
        amount_paid = amount_paid * 0.0072
        item_cost = item_cost * 0.0072 
        pass 
    #create a dictionairy to hold the values / keep track of the change 
    
    

    def change_euros(amount_paid, item_cost):
        pass

    def change_ruble(amount_paid, item_cost):
       pass
    
    

print(exact_change(100,62.13))
    



