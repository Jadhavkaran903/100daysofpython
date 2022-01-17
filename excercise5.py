# Your life in weeks
age=input('What is your current age?')

age_as_int=int(age)

year_remaining=90-age_as_int
days_remaining=year_remaining*365
weeks_remaining=year_remaining*52
months_remaining=year_remaining*12

print(f"You have {year_remaining} years,{days_remaining} days,{weeks_remaining} weeks,{months_remaining} months left")