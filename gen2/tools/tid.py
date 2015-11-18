from colorama import init, Fore
init()

while True:
  tid = int(input("What is your TID? "))

  if   tid >= 55296 and tid <= 55551:
    print(Fore.GREEN + "Valid TID!", Fore.RESET + "D8")
  elif tid >= 55552 and tid <= 55807:
    print(Fore.GREEN + "Valid TID!", Fore.RESET + "D9")
  elif tid >= 63488 and tid <= 63743:
    print(Fore.GREEN + "Valid TID!", Fore.RESET + "F8")
  elif tid >= 63744 and tid <= 63999:
    print(Fore.GREEN + "Valid TID!", Fore.RESET + "F9")
  else:
    print(Fore.RED + "Not a valid TID, sorry! Reset!" + Fore.RESET)