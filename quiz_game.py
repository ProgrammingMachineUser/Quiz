print("Welcome to my computer quiz!")

playing = input("Do you want to play?")

if playing.upper() != "YES":
    quit()

print("Ok! Let's play :)!")
score = 0

answer = input("What does CPU stand for?")
if answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for?")
if answer == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
answer = input("What does RAM stand for?")
if answer == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
answer = input("What does PSU stand for?")
if answer == "power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
print("your score is: ", score)
if score == 0:
    print("horrible")
if score == 1:
    print("bad")
if score == 2:
    print("decent")
if score == 3:
    print("good")
if score == 4:
    print("GG!")