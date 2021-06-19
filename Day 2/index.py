# Tip Calculator

# Initializing the variables as empty strings since teh input() returns strings
base_bill = ""
percentage = ""
people = ""

print("Welcome to the tip calculator");

# Creating the bill without the tip
while True: 
  print("What was the total amount of the bill?")
  base_bill = input(">Rs.")

  # Check if the value can be converted to float
  try:
    float(base_bill)
    # Check if the number is not a negative number 
    # 0 is fine as due to offer the bill can be set as free
    if float(base_bill) < 0:
      print("Please enter a positive amount, bill cannot be negative")
    else:
      break
  #if not, ask again 
  except ValueError:
    print("Please enter a valid amount")

# Getting the percentage for the tip
while True:
  print('What percentage would you like to give a tip as? 10 , 12 or 15?')
  percentage = input('>')
  # Give the choices list and check for the values
  choices_list = ["10" , "12", "15"]
  # Check if the value is from the string 
  if percentage not in choices_list:
    print('Please enter 10,12 or 15')
  else:
    break

# Get the number of people 
while True:
  print('How many people to split the bill for?')
  people = input('>')
  # Check if the number is a natural number and non zero
  if not people.isdigit() or people == "0":
    print('Please enter a valid value')
  else:
    break

#Adding the tip to the total bill value 
total_bill = float(base_bill) * (1 + int(percentage)/100)

# Calculate the split bill and round off to 2 decimal places 
split_bill = round(total_bill/int(people), 2)

# Printing the total bill value 
print(f"Each person has to pay Rs.{split_bill}")