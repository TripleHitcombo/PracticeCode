name = input ("What is your name? ")
print("Welcome", name, "to this adventure!")

answer = input ("You are on a dirt road it has come to and. You can go left or right. Which way would you like to go?: " ).lower()

if answer == "left":
    answer = input ("You come to a river, you can walk around it or swim across. (walk/swim) ").lower()

    if answer == "swim":
        print("You swam across and was eaten by a crocodile")

    elif answer == "walk":
        print("You walked for many miles and exhausted all of your supplies. You died!")

    else:
        print("Not a valid option. You lose")

elif answer == "right":
    answer = input ("You come to a bridge, it looks wobbly. Do you want to cross it or head back? (Cross/Back)").lower()

    if answer == "back":
        print("You go back and get eaten by a leopard on the way!")

    elif answer == "cross":
        print("You cross the bridge and meet a stranger. Do you talk to them? (yes/no) ")

        if answer == "yes":
            print ("The stranger offers to take you into town!")

        elif answer == "no":
            print ("You try to cross the bridge again and it collapses!")

        else:
            print("Not a valid option. You lose")

    else:
        print("Not a valid option. You lose")

else:
    print ("Not a valid option. You lose")