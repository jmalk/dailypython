# A simple interest calculator
# Given an initial deposit, interest rate, and amount of years to leave the money in the account for, calculate the final account balance.

# TODO: format output to sensible length e.g. 2 decimal places.

initial_deposit = float(raw_input("How much do you wish to deposit? "))
interest_rate = float(raw_input("What is the annual interest rate of your account? "))
time_saved_for = float(raw_input("How many years do you wish to save the money for? "))

# Turn interest rate into a factor, e.g. 5% -> 1.05
interest_factor = 1.0 + interest_rate / 100.0

final_balance = initial_deposit * pow(interest_factor, time_saved_for)

print("Saving an initial deposit of %(deposit)2f for %(time)2f years at an annual interest rate of %(rate)2f%% will result in a final account balance of %(balance)2f .") % \
        {"deposit": initial_deposit, "time": time_saved_for, "rate": interest_rate, "balance": final_balance}
