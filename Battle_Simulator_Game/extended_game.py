
# Extended version of the simulator
# Includes basic game and extension is added

# For this extended version of the basic game
# Medics and Expanded armies were added!

print("Welcome to the Battle Simulator!")

# Get participant ready

initial_response = input("Are you ready to demonstrate your military prowess Commander?? (y/n) ")
response = ""

# Army selection variables

army_1 = []
army_2 = []
balance_1 = 10
balance_2 = 10

units = ["Archer", "Knight", "Soldier", "Siege Equipment", "Wizard"]
a = units[0]
k = units[1]
s = units[2]
se = units[3]
w = units[4]

# Choosing the first army

first_army = str(input("Enter the name of your first army: "))
print("Welcome " + first_army + ", time to choose your troops!")

# This loop will continue to ask for a unit purchase
# That is until either condition is broken
# Or exit condition fulfilled
# Each choice is appended to a list
# That way we make sure the list is in order

while initial_response == "y" and 0 < balance_1 <= 10:
    response = str(input("""Purchase an army unit:
              1 for Archer
              2 for Knight
              3 for Soldier
              4 for Siege Equipment
              5 for Wizard
              6 to Exit """))

    if str(response) == "1":
        army_1.append(a)
        balance_1 = balance_1 - 1
        print(army_1)
        print("$" + str(balance_1) + " remaining")

    elif str(response) == "2":
        army_1.append(k)
        balance_1 = balance_1 - 1
        print(army_1)
        print("$" + str(balance_1) + " remaining")

    elif str(response) == "3":
        army_1.append(s)
        balance_1 = balance_1 - 1
        print(army_1)
        print("$" + str(balance_1) + " remaining")
        
# The following condition refers to the siege equipment
# Because he is more powerful he gets double the value
# The wizard is even more powerful
# Couldn't make him anymore expensive, otherwise teams would have little room for medics

    elif str(response) == "4":
        army_1.append(se)
        balance_1 = balance_1 - 2
        print(army_1)
        print("$" + str(balance_1) + " remaining")
        
# As mentioned above, the wizard is most powerful
# As a result he gets the highest value

    elif str(response) == "5":
        army_1.append(w)
        balance_1 = balance_1 - 3
        print(army_1)
        print("$" + str(balance_1) + " remaining")

    elif str(response) == "6":
        print("Your army is made up of ", army_1, "and you have $", balance_1, " remaining")
        break

# Choosing the second army for combat

second_army = str(input("Enter the name of your second army: "))
print("Welcome " + second_army + ", time to choose your troops!")

# This loop will continue to ask for a unit purchase
# That is until either condition is broken
# Or exit condition fulfilled
# Each choice is appended to a list
# That way we make sure the list is in order

while initial_response == "y" and 0 < balance_2 <= 10:
    response = str(input("""Purchase an army unit:
              1 for Archer
              2 for Knight
              3 for Soldier
              4 for Siege Equipment
              5 for Wizard
              6 to Exit """))
    if str(response) == "1":
        army_2.append(a)
        balance_2 = balance_2 - 1
        print(army_2)
        print("$" + str(balance_2) + " remaining")

    elif str(response) == "2":
        army_2.append(k)
        balance_2 = balance_2 - 1
        print(army_2)
        print("$" + str(balance_2) + " remaining")

    elif str(response) == "3":
        army_2.append(s)
        balance_2 = balance_2 - 1
        print(army_2)
        print("$" + str(balance_2) + " remaining")
        
# The following condition refers to the siege equipment
# Because he is more powerful he gets double the value
# The wizard is even more powerful
# Couldn't make him anymore expensive, otherwise teams would have little room for medics

    elif str(response) == "4":
        army_2.append(se)
        balance_2 = balance_2 - 2
        print(army_2)
        print("$" + str(balance_2) + " remaining")
        
# As mentioned above, the wizard is most powerful
# As a result he gets the highest value

    elif str(response) == "5":
        army_2.append(w)
        balance_2 = balance_2 - 3
        print(army_2)
        print("$" + str(balance_2) + " remaining")

    elif str(response) == "6":
        print("Your army is made up of ", army_2, "and you have $", balance_2, " remaining\n")
        break

# To incorporate medics we created a list of medics for each army
# Makes it much easier to work into the conditions below
# To calculate how many each army should have
# Used the remaining balance to inform how many an army will have

medics_1 = ["Medic"] * balance_1
medics_2 = ["Medic"] * balance_2
print("Army 1 has", balance_1, "medics\n", medics_1)
print("Army 2 has", balance_2, "medics\n", medics_2, "\n")


print("The first army consists of: ", army_1, "and", medics_1)
print("The second army consists of: ", army_2, "and", medics_2, "\n")
print("The army with units remaining at the end of battle, wins.\n")
print("Battle lines have been drawn, it's now time to duel!\n")

# In order to pull out units in order for battle
# The conditions will show the use of the pop function
# Pop only takes from the end of a list
# Using a reverse of the list will allow us to maintain the order of purchase

reversed_army1 = reversed(army_1)
reversed_army1 = list(reversed_army1)

reversed_army2 = reversed(army_2)
reversed_army2 = list(reversed_army2)

# In order to initiate combat, I need some sort of condition
# The following format made it easy to format the duels
# Straightforward comparisons of x and y help keep the code simple

i = 0
while i != 1:

    x = reversed_army1.pop()
    y = reversed_army2.pop()
    print(x, "&", y)

# Conditions of battle

# The following lists all the conditions and possible battle combinations
# That could take place during the simulator, in accordance with assignment rules

    if x == "Archer" and y == "Archer":
        print("It's a tie!")
        if len(medics_1) > 0:
            medics_1.pop()
            reversed_army1.insert(0, "Archer")
        if len(medics_2) > 0:
            medics_2.pop()
            reversed_army2.insert(0, "Archer")
            
# In tie situations, when medics are available
# Both sides will have their units returned to the end of their lists

        print("\nArmy 1: ", list(reversed(reversed_army1)))
        print("Army 2: ", list(reversed(reversed_army2)))
        
# Reversed list of the reversed list is to make sure the user sees the list in order
# Once the duel is over.
# I tried to store this value in another list
# But because we are using the pop function
# We are in constant need of the reverse of the list
# Meaning we would have to go back and forth between two lists

    elif x == "Archer" and y == "Knight":
        reversed_army2.append("Knight")
        if len(medics_1) > 0:
            medics_1.pop()
            reversed_army1.insert(0, "Archer")
            
# The above if condition for medics allows for easy use after duel outcomes
# The insertion at the start of the list of the healed unit
# Again comes back to the fact we are using reversed lists and pop function
# Inserting at the start of a reversed list, means at the end of the real list

        print("The knight is victorious!")
        print("\nArmy 1: ", list(reversed(reversed_army1)))
        print("Army 2: ", list(reversed(reversed_army2)))

    elif x == "Knight" and y == "Archer":
        reversed_army1.append("Knight")
        if len(medics_2) > 0:
            medics_2.pop()
            reversed_army2.insert(0, "Archer")

        print("The knight is victorious!")
        print("\nArmy 1: ", list(reversed(reversed_army1)))
        print("Army 2: ", list(reversed(reversed_army2)))

    elif x == "Archer" and y == "Soldier":
        reversed_army1.append("Archer")
        if len(medics_2) > 0:
            medics_2.pop()
            reversed_army2.insert(0, "Soldier")

        print("The archer is victorious!")
        print("\nArmy 1: ", list(reversed(reversed_army1)))
        print("Army 2: ", list(reversed(reversed_army2)))

    elif x == "Soldier" and y == "Archer":
        reversed_army2.append("Archer")
        if len(medics_1) > 0:
            medics_1.pop()
            reversed_army1.insert(0, "Soldier")

        print("The archer is victorious!")
        print("\nArmy 1: ", list(reversed(reversed_army1)))
        print("Army 2: ", list(reversed(reversed_army2)))

    elif x == "Knight" and y == "Knight":
        print("It's a tie!")
        if len(medics_1) > 0:
            medics_1.pop()
            reversed_army1.insert(0, "Knight")
        if len(medics_2) > 0:
            medics_2.pop()
            reversed_army2.insert(0, "Knight")
            
        print("\nArmy 1: ", list(reversed(reversed_army1)))
        print("Army 2: ", list(reversed(reversed_army2)))

    elif x == "Knight" and y == "Soldier":
        reversed_army2.append("Soldier")
        if len(medics_1) > 0:
            medics_1.pop()
            reversed_army1.insert(0, "Knight")

        print("The soldier is victorious!")
        print("\nArmy 1: ", list(reversed(reversed_army1)))
        print("Army 2: ", list(reversed(reversed_army2)))

    elif x == "Soldier" and y == "Knight":
        reversed_army1.append("Soldier")
        if len(medics_2) > 0:
            medics_2.pop()
            reversed_army2.insert(0, "Knight")

        print("The soldier is victorious!")
        print("\nArmy 1: ", list(reversed(reversed_army1)))
        print("Army 2: ", list(reversed(reversed_army2)))

    elif x == "Soldier" and y == "Soldier":
        print("It's a tie!")
        if len(medics_1) > 0:
            medics_1.pop()
            reversed_army1.insert(0, "Soldier")
        if len(medics_2) > 0:
            medics_2.pop()
            reversed_army2.insert(0, "Soldier")
            
        print("\nArmy 1: ", list(reversed(reversed_army1)))
        print("Army 2: ", list(reversed(reversed_army2)))

    elif x == "Siege Equipment" and y == "Knight":
        reversed_army2.append("Knight")
        if len(medics_1) > 0:
            medics_1.pop()
            reversed_army1.insert(0, "Siege Equipment")

        print("The knight is victorious!")
        print("\nArmy 1: ", list(reversed(reversed_army1)))
        print("Army 2: ", list(reversed(reversed_army2)))

    elif x == "Siege Equipment" and y == "Soldier":
        reversed_army1.append("Siege Equipment")
        if len(medics_2) > 0:
            medics_2.pop()
            reversed_army2.insert(0, "Soldier")

        print("The siege equipment is victorious!")
        print("\nArmy 1: ", list(reversed(reversed_army1)))
        print("Army 2: ", list(reversed(reversed_army2)))

    elif x == "Siege Equipment" and y == "Archer":
        reversed_army1.append("Siege Equipment")
        if len(medics_2) > 0:
            medics_2.pop()
            reversed_army2.insert(0, "Archer")

        print("The siege equipment is victorious!")
        print("\nArmy 1: ", list(reversed(reversed_army1)))
        print("Army 2: ", list(reversed(reversed_army2)))

    elif x == "Siege Equipment" and y == "Wizard":
        reversed_army2.append("Wizard")
        if len(medics_1) > 0:
            medics_1.pop()
            reversed_army1.insert(0, "Siege Equipment")

        print("The wizard is victorious!")
        print("\nArmy 1: ", list(reversed(reversed_army1)))
        print("Army 2: ", list(reversed(reversed_army2)))

    elif x == "Siege Equipment" and y == "Siege Equipment":
        print("It's a tie!")
        if len(medics_1) > 0:
            medics_1.pop()
            reversed_army1.insert(0, "Siege Equipment")
        if len(medics_2) > 0:
            medics_2.pop()
            reversed_army2.insert(0, "Siege Equipment")
            
        print("\nArmy 1: ", list(reversed(reversed_army1)))
        print("Army 2: ", list(reversed(reversed_army2)))

    elif x == "Knight" and y == "Siege Equipment":
        reversed_army1.append("Knight")
        if len(medics_2) > 0:
            medics_2.pop()
            reversed_army2.insert(0, "Siege Equipment")

        print("The knight is victorious!")
        print("\nArmy 1: ", list(reversed(reversed_army1)))
        print("Army 2: ", list(reversed(reversed_army2)))

    elif x == "Soldier" and y == "Siege Equipment":
        reversed_army2.append("Siege Equipment")
        if len(medics_1) > 0:
            medics_1.pop()
            reversed_army1.insert(0, "Soldier")

        print("The siege equipment is victorious!")
        print("\nArmy 1: ", list(reversed(reversed_army1)))
        print("Army 2: ", list(reversed(reversed_army2)))

    elif x == "Archer" and y == "Siege Equipment":
        reversed_army2.append("Siege Equipment")
        if len(medics_1) > 0:
            medics_1.pop()
            reversed_army1.insert(0, "Archer")

        print("The siege equipment is victorious!")
        print("\nArmy 1: ", list(reversed(reversed_army1)))
        print("Army 2: ", list(reversed(reversed_army2)))

    elif x == "Wizard" and y == "Siege Equipment":
        reversed_army1.append("Wizard")
        if len(medics_2) > 0:
            medics_2.pop()
            reversed_army2.insert(0, "Siege Equipment")

        print("The wizard is victorious!")
        print("\nArmy 1: ", list(reversed(reversed_army1)))
        print("Army 2: ", list(reversed(reversed_army2)))

    elif x == "Wizard" and y == "Wizard":
        print("It's a tie!")
        if len(medics_1) > 0:
            medics_1.pop()
            reversed_army1.insert(0, "Wizard")
        if len(medics_2) > 0:
            medics_2.pop()
            reversed_army2.insert(0, "Wizard")
            
        print("\nArmy 1: ", list(reversed(reversed_army1)))
        print("Army 2: ", list(reversed(reversed_army2)))

    elif x == "Knight" and y == "Wizard":
        reversed_army2.append("Wizard")
        if len(medics_1) > 0:
            medics_1.pop()
            reversed_army1.insert(0, "Knight")

        print("The wizard is victorious!")
        print("\nArmy 1: ", list(reversed(reversed_army1)))
        print("Army 2: ", list(reversed(reversed_army2)))

    elif x == "Soldier" and y == "Wizard":
        reversed_army2.append("Wizard")
        if len(medics_1) > 0:
            medics_1.pop()
            reversed_army1.insert(0, "Soldier")

        print("The wizard is victorious!")
        print("\nArmy 1: ", list(reversed(reversed_army1)))
        print("Army 2: ", list(reversed(reversed_army2)))

    elif x == "Archer" and y == "Wizard":
        reversed_army1.append("Archer")
        if len(medics_2) > 0:
            medics_2.pop()
            reversed_army2.insert(0, "Wizard")

        print("The archer is victorious!")
        print("\nArmy 1: ", list(reversed(reversed_army1)))
        print("Army 2: ", list(reversed(reversed_army2)))

    elif x == "Wizard" and y == "Knight":
        reversed_army1.append("Wizard")
        if len(medics_2) > 0:
            medics_2.pop()
            reversed_army2.insert(0, "Knight")

        print("The wizard is victorious!")
        print("\nArmy 1: ", list(reversed(reversed_army1)))
        print("Army 2: ", list(reversed(reversed_army2)))

    elif x == "Wizard" and y == "Soldier":
        reversed_army1.append("Wizard")
        if len(medics_2) > 0:
            medics_2.pop()
            reversed_army2.insert(0, "Soldier")

        print("The wizard is victorious!")
        print("\nArmy 1: ", list(reversed(reversed_army1)))
        print("Army 2: ", list(reversed(reversed_army2)))

    elif x == "Wizard" and y == "Archer":
        reversed_army2.append("Archer")
        if len(medics_1) > 0:
            medics_1.pop()
            reversed_army1.insert(0, "Wizard")

        print("The archer is victorious!")
        print("\nArmy 1: ", list(reversed(reversed_army1)))
        print("Army 2: ", list(reversed(reversed_army2)))

# This refers to when either list is empty and need to decide winner

    if len(reversed_army1) < 1:
        print(second_army.upper(), "(Army 2) IS VICTORIOUS!")
        print("\nRemaining units of Army 2: ", list(reversed(reversed_army2)))
        break

    elif len(reversed_army2) < 1:
        print(first_army.upper(), "(Army 1) IS VICTORIOUS!")
        print("\nRemaining units of Army 1: ", list(reversed(reversed_army1)))
        break

    elif len(reversed_army1) < 1 and len(reversed_army2) < 1:
        print("Both armies have lost all units!\nIt's a tie!")
        break

print("\nThank you for playing. If you really liked our simulator, you can always start again.")

# That's all she wrote folks!

