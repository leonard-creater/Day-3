weight=float(input("entry you weight"))
height=float(input("entry you height"))

BMI=weight/(height/100)**2
print("You BMI is")

if BMI <=20:
  print("your under-weight")

elif BMI<=25:
  print("your in good health")

elif BMI<=30:
  print("your obesse")

else :
  print("Go see a doctor")