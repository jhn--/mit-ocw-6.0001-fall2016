annual_salary = float(input("Enter the starting salary: "))
total_cost = 1_000_000.00
semi_annual_raise = 0.07
portion_down_payment = 0.25 * total_cost
current_savings = 0.0
r = 0.04

count = 0
mod = 6
months = 36

monthly_salary = annual_salary / 12
total_salary = 0

portion_saved = 10_000
epsi = 100.0 

low = 0
mid = portion_saved / 2.0
high = portion_saved

# print(f'portion_down_payment: {portion_down_payment}\n')

for i in range(months):
    # let's check the total salary of 36 months after the -
    # 1. semi_annual_raise
    # 2. r (investment returns)
    # and see if it (100%) is more than portion_down_payment
    if i != 1 and i % mod == 1:
        monthly_salary *= 1 + semi_annual_raise
    monthly_salary += monthly_salary * (r / 12)
    total_salary += monthly_salary
if total_salary < portion_down_payment:
    # if it is not, then there's no point continuing
    print('It is not possible to pay the down payment in three years.')
else:
    # there is a chance, now let's find how much % we'll need to save
    # print(f'total salary: {total_salary}')
    saved = total_salary * (mid / portion_saved) # let's start with 50% saved
    # I think count should +1 here actually. because we kinda start here didn't we?
    while abs(portion_down_payment - saved) > epsi: # while the differences is > 100$
        count += 1 # increase count by 1
        if portion_down_payment > saved: # if downpayment is more than saved amount (saved)
            print("down payment is higher\n")
            low = mid # let's make mid the new low
        else: # downpayment is lesser than saved amount (saved)
            print("down payment is lower\n")
            high = mid # let's mid the new high
        mid = (low + high) / 2.0 # get the new value of mid
        saved = total_salary * (mid / portion_saved) # calculate the new saved amount using new mid
            
    print(f"Best savings rate: {mid / portion_saved}")
    print(f"Steps in bisection search: {count}")
