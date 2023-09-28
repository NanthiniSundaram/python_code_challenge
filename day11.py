#challenge_day11

print("Check how many seconds you have in a year here!!!")
print("-------------------------------------------------")
year=int(input("Enter the year >"))
if (year%400==0) and (year%100==0):
  print("The year",year,"is a leap year")
  print("""You have 12 months 
           52 weeks
           366 days
           24 hrs in oneone day
           60 min in one hour
           60 min in one minute 
           """)
  seconds=366*24*60*60
  print("Ohh!! You have",seconds,"Seconds!!")
elif (year%4==0) and (year%100!=0):
  print("The year",year,"is a leap year")
  print("""You have 12 months 
           52 weeks
           366 days
           24 hrs in oneone day
           60 min in one hour
           60 min in one minute
           """)
  seconds=366*24*60*60
  print("Ohh!! You have",seconds,"Seconds!!")
  
else:
  print("The year",year,"is not a leap year")
  print("""You have 12 months 
           52 weeks
           365 days
           24 hrs in oneone day
           60 min in one hour
           60 min in one minute 
           """)
  seconds=365*24*60*60
  print("Ohh!! You have",seconds,"Seconds!!")
  
