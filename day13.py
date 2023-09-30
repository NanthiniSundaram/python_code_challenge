#challenge_day13

print("EXAM GRADE CALCULATOR")
print("----------------------")
exam=input("Enter the name of your exam >")
max_marks=int(input("Enter the maximum mark >"))
your_mark=int(input("Enter your score >"))
percent=(your_mark/max_marks)*100
grade=round(percent,2)
if grade>=90 and grade<=100:
  print("Congrats!! Your score is",percent,"and grade is A+")
elif grade>=80 and grade<=89:
  print("Congrats!! Your score is",percent, "and grade is A")
elif grade>=70 and grade<=79:
  print(" Your score is",percent ,"and grade is B")  
elif grade>=60 and grade<=69:
  print("Your score is",percent ,"and grade is C")
elif grade>=50 and grade<=59:
  print("Your score is",percent ,"and  grade is D")
else:
  print("Your score is",percent ,"and  grade is U")
