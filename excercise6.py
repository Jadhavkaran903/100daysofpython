# Tip calulator
bill=int(input("What was the total bill"))
tip=int(input("What percentage tip would you like to give"))
members=int(input("How many people to split the bill"))

tip_cal=(bill/members)*(tip/100)
total_bill=(bill/members)+tip_cal

print(f"Each person should pay {total_bill} rupees")