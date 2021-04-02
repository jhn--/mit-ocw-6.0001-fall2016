'''
Part B: Saving, with a raise 

Background 

In Part A, we unrealistically assumed that your salary didn’t change. But you are an MIT graduate, 
and clearly you are going to be worth more to your company over time! So we are going to build on your solution to Part A by factoring in a raise every six months. 

In ps1b.py, copy your solution to Part A (as we are going to reuse much of that machinery). 
Modify your program to include the following 

1.Have the user input a semi-annual salary raise semi_annual_raise (as a decimal percentage) 
2.After the 6 th month, increase your salary by that percentage. Do the same after the 12th th month, the 18 month, and so on. 

Write a program to calculate how many months it will take you save up enough money for a down payment. 
LIke before, assume that your investments earn a return of r = 0.04 (or 4%) and the required down payment percentage is 0.25 (or 25%). 
Have the user enter the following variables:
1.The starting annual salary (annual_salary) 2
2.The percentage of salary to be saved (portion_saved) 
3.The cost of your dream home (total_cost) 
4.The semiannual salary raise (semi_annual_raise) 

Hints

To help you get started, here is a rough outline of the stages you should probably follow in writing your code: 
●Retrieve user input. 
●Initialize some state variables. You should decide what information you need. Be sure to be careful about values that 
represent annual amounts and those that represent monthly amounts. 
●Be careful about when you increase your salary – this should only happen after the 6 th , 12th , 18th month, and so on.
'''

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))
portion_down_payment = 0.25 * total_cost
current_savings = 0.0
r = 0.04

count = 0
mod = 6

while current_savings <= portion_down_payment:
    if count != 1 and count % mod == 1:
        annual_salary *= 1 + semi_annual_raise
        current_savings += ((annual_salary/12)*portion_saved) + (current_savings*(r/12))
    else:
        current_savings += ((annual_salary/12)*portion_saved) + (current_savings*(r/12))
        
    count += 1
print(f"Number of months: {count}")
