# Creating the Band name generator

print('Welcome to the Band Name generator');

#initializing the variables as empty strings 
city = ""
pet_name =""

# To check if the user has entered something in the city field
while True:
  print("What is the name of the city that you grew up in?")
  city = input(">")
  # if there is no input ask again 
  if city == "":
    print("You haven't entered anything, please enter")
  else:
    break

# To check if the user has entered something in the pet_name field 
while True:
  print("Enter the name of your current pet")
  pet_name = input(">")
  #checking if the user has entered anything 
  if pet_name == "":
    print("You have not entered anything, please enter")
  else:
    break

#Setting the output that makes the code more readable 
print(f"The name of your band could be {city} {pet_name} ")