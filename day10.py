#challenge_day10

print("Tip Calculator")
print("---------------")
cost=float(input("How much did you spend >"))
tip=int(input("What percentage do you want to tip >"))
group=int(input("How many people in your group >"))
tip_amount=tip/100*cost
amount=cost+tip_amount
share=amount/group
share=round(share,2)
print("Each of you should pay",share)
