import datetime
import calendar


# balance = 5000
# interest_rate = 13 * .01
# monthly_payment = 500

# today = datetime.date.today()
# days_in_current_month = calendar.monthrange(today.year, today.month)[1]
# days_till_end_month = days_in_current_month - today.day

# start_date = today + datetime.timedelta(days=days_till_end_month + 1)
# end_date = start_date

# while balance > 0:
#     interest_charge = (interest_rate / 12) * balance
#     balance += interest_charge
#     balance -= monthly_payment

#     balance = 0 if balance < 0 else round(balance, 2)

#     print(end_date, balance)

#     days_in_current_month = calendar.monthrange(end_date.year, end_date.month)[1]
#     end_date = end_date + datetime.timedelta(days=days_in_current_month)



current_weight = 220
goal_weight = 180
avg_lbs_week = 1.5

start_date = datetime.date.today()
end_date = start_date

while current_weight > goal_weight:
    end_date += datetime.timedelta(days=7)
    current_weight -= avg_lbs_week

print(end_date)
print(f"Reached goal in {(end_date - start_date).days // 7} weeks")
