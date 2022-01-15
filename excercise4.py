height=input("enter your height in m: ")
weight=input("enter your weight in kg: ")

bmi_cal=int(weight)/float(height)**2
bmi_result=int(bmi_cal)
print("Your BMI is " + str(bmi_result))

