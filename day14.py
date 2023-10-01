#challenge-day14
#rock paper scissor game

from getpass import getpass as input
print("It's a Rock Paper Scissor Battle")
print("Select your move as R,P or S")
player_1=input("Enter your name >")
player_2=input("Enter your name >")
move_pl1=input("Enter your move >")
move_pl2=input("Enter your move >")
if move_pl1=="R":
  if move_pl2=="S":
    print("Congrats!!",player_1,"won the battle😉.")
  elif move_pl2=="P":
    print("Congrats!!",player_2,"won the battle😉.")
  else:
    print("Ohh!! It's a draw")
elif move_pl1=="P":
  if move_pl2=="S":
    print("Congrats!!",player_2,"won the battle😉.")
  elif move_pl2=="R":
    print("Congrats!!",player_1,"won the battle😉.")
  else:
    print("Ohh!! It's a draw")
elif move_pl1=="S":
  if move_pl2=="R":
    print("Congrats!!",player_2,"won the battle😉.")
  elif move_pl2=="P":
    print("Congrats!!",player_1,"won the battle😉.")
  else:
    print("Ohh!! It's a draw")
else:
  print("Sorry,could not process command try giving R,P OR S.")
