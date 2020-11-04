import re

while True:
  user_input = input("Enter a password : ")
  is_valid = False

  if (len(user_input)<8 or len(user_input)>20):
    print("Not valid ! Total characters should be between 8 and 20")
    continue
  elif not re.search("[A-Z]",user_input):
    print("Not valid ! It should contain one letter between [A-Z]")
    continue
  elif not re.search("[a-z]",user_input):
    print("Not valid ! It should contain one letter between [a-z]")
    continue
  elif not re.search("[1-9]",user_input):
    print("Not valid ! It should contain one letter between [1-9]")
    continue
  elif not re.search("[!?=#]",user_input):
    print("Not valid ! It should contain at least one letter in [!?=#]")
    continue
  else:
    is_valid = True
    break

if(is_valid):
  print("Password is valid")