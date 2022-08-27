# Name: Biki Gurung
# Date: 08/27/22
# Description: Update the server, ask the user if they will like to upgrade, and save results to a file.

import os

os.system('sudo apt-get update -y > info.txt 2> error.txt')

print("Update Sucessful")
print("\n==========Update Info Message==========\n")
os.system('cat info.txt')

print("\n==========Update Error Message=========\n")
os.system('cat error.txt')

userInput = input("\nWould you like to upgrade your server? Y/N : ")

if userInput.lower() == 'y':
  os.system('sudo apt-get upgrade -y >> info.txt 2>> error.txt')
  print("\nUpgrade Complete\n")
  print("\n==========Upgrade Info Message Added==========\n")
  os.system('cat info.txt')
  print("\n==========Upgrade Error Message Added=========\n")
  os.system('cat error.txt')
