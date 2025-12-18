def house_summary():
    """------------------------------------------------------
    a program with two inputs, current price and last
    month's price (both integers). Then, outputs a summary
    listing the price, the change since last month, and
    the estimated monthly mortgage computed as
    (current_price * 0.051) / 12.
    """
    print(house_summary.__doc__)

    current_price = int(input())
    last_months_price = int(input())
    mortgage = (current_price * 0.051) / 12

    print(f'This house is ${current_price:.0f}. The change is $'
          f'{current_price - last_months_price} since last month.')
    print(f'The estimated monthly mortgage is ${mortgage:.2f}.')
    print('------------------------------------------------------')
