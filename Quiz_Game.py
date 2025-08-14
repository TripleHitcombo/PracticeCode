print ("Welcome to the Quiz Game!")

playing = input("Do you want to play? ")

if playing.lower() != "yes": # .lower() forces the string to always use lower case .upper() for upper case
    quit()

print("Okay, let's play!")
score = 0

answer = input("What colour is a banana? ")
if answer.lower() == "yellow":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What sound does a dog make? ")
if answer.lower() == "woof":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is 5 + 5? ")
if answer.lower() == "10":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What creature has eight legs? ")
if answer.lower() == "spider":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What creature breathes fire? ")
if answer.lower() == "dragon":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print ("You got " + str(score) + "/5 questions corrct")

#Area for improvement: Categorise questions and add more, add leaderbpard, add UI with images and sounds, deduct points on incorrect questions. 

