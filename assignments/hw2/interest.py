"""
Name: Angela Nganga
interest.py

Problem: This function computes the monthly interest charge on a credit card account.

Certification of Authenticity:
I cerify that this assignment is my own work, but I discussed it with tutors at the CSL.
"""

def main():
    annual_interest_rate = eval(input(" Enter the annual interest rate: "))
    annual_interest_rate/=100
    days_in_billing_cycle = eval(input("Enter the number of days in the billing cycle: "))
    net_balance = eval(input("Enter the previous balance: "))
    net_payment = eval(input("Enter the payment amount: "))
    day_of_payment = eval(input("Enter the day of billing cycle when the payment was made: "))
    step1 = net_balance * days_in_billing_cycle
    step2 = net_payment * (days_in_billing_cycle - day_of_payment)
    step3 = step1-step2
    avg_daily_bal = step3 / days_in_billing_cycle
    monthly_interest = annual_interest_rate/12
    monthly_interest_charge = avg_daily_bal * monthly_interest
    monthly_interest_charge = round(monthly_interest_charge, 2)
    print(monthly_interest_charge)


if __name__=='__main__':
    main()
