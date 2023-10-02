#challenge_day15

print("Get the sounds of your favourite animals here!!")
exit=""
while exit!="yes":
  animal=input("What animal do you want >")
  if animal=="Cow" or animal=="cow":
    print("A cow goes moooo!")
  elif animal=="Dog" or animal=="dog":
    print("A dog goes bowwbowww!")
  elif animal=="Cat" or animal=="cat":
    print("A cat goes meowww!")
  elif animal=="goat" or animal=="Goat":
    print("A goat goes baaa!")
  elif animal=="Sheep" or animal=="sheep":
    print("A sheep goes baaa!")
  elif animal=="Donkey" or animal=="donkey":
    print("A donkey goes hee-haww!")
  elif animal=="horse" or animal=="Horse":
    print("A horse goes neighh!")
  elif animal=="lemur" or animal=="Lemur":
    print("A lemur goes awooga!")
  else:
    print("Sorry, try with an another animal")
  exit=input("Do you want to exit?")
  
