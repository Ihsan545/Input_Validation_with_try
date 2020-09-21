"""
Program: percent_coupon.py.
Author: Ihsanullah Anwary
Last date modified: 09/21/2020

 program is example of nested if using calculations.
"""


def calculate_order(price):  # Function definition.
    cash_off_per_order= 5.00
    coupons_percentage = 5.99

    if price > 15: # price over 15
        tax = 30
        # calculation
        total_price = price - cash_off_per_order
        total_percentage = total_price / 100 * tax
        total_discount = total_price - total_percentage
        get_tax = total_discount / 100 * 6
        add_tax = get_tax + total_discount
        total = add_tax + coupons_percentage
        return total

    if price == 10 and price < 30:  # 10 to up to 30, 5 cash, 10%
        tax = 30
        return tax

    if price == 10 and price <= 50: # 30 to up to 50, 5 cash, 10%
        tax = 10
        return tax

    if price > 50: # 50 and above, 5 cash, 10%
        tax = 10
        return tax


if __name__ == '__main__':
    print(calculate_order(20))
    print(calculate_order(22))
    print(calculate_order(30))
    print(calculate_order(55))
