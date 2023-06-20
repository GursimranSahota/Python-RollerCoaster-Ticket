print("Welcome to the Roller Coaster Ride!")
height = int(input("Enter your height in cm: "))
print("\n")
bill = 0
if height >= 120 :
  print("Great! You can ride the roller coaster ")
  print("\n")
  age = int(input("How old are you? "))
  if age < 12 :
    bill = 5
    print("Child tickets are 5 dollars")
  elif age <= 18 :
    bill = 7
    print("Youth tickets are 7 dollars")
  else :
    bill = 12
    print("Adult tickets are 12 dollars")
  print("\n")
  wants_photo = input("Would you like a photo? Enter 'Y' for Yes, or 'N' for No: ")
  if wants_photo == "Y" :
    bill += 3
    print(f"Your final bill is {bill} dollars")
  else:
    print(f"Your final bill is {bill} dollars")
else :
  print("Sorry, you are not tall enough to ride this roller coaster ")