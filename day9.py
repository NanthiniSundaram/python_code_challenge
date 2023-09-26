#challenge_day9

print("**Generation Identifier**")
print("---------------------------")
year=int(input("Which year were you born >"))
if year>=1883 and year<=1900:
    print("Heyy!! You belong to lost generation!!")
elif year>=1901 and year<=1927:
  print("Heyy!! You belong to Greatest generation!!")
elif year>=1928 and year<=1945:
  print("Heyy!! You belong to silent generation!!")
elif year>=1946 and year<=1964:
  print("Heyy!! You belong to Baby boomers!!")
elif year>=1965 and year<=1980:
  print("Heyy!! You belong to Greatest X!!")
elif year>=1981 and year<=1996:
  print("Heyy!! You belong to Millenial!!")
elif year>=1997 and year<=2012:
  print("Heyy!! You belong to Greatest Z!!")
elif year>=2013:
  print("Heyy!! You belong to Alpha generation!!")
else:
  print("Sorry!! Year out of range")
