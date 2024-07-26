from gameData import data
import random
def randomSelect():
    ran = random.choice(data)
    return ran
def is_higher(inp,ran1F,ran2F):
    if ran1F > ran2F:
        return inp == 'a'
    else:
        return inp == 'b'      
score = 0
ran2 = randomSelect()
play = True
while play:
    ran1 = ran2
    ran2 = randomSelect()
    if ran1 == ran2:
        ran2=randomSelect()
    print(f'your current score is {score}')
    print(f"{ran1['name']}, a {ran1['description']}, from {ran1['country']}")
    print("VS")
    print(f"{ran2['name']}, a {ran2['description']}, from {ran2['country']}")
    user_input = input("who has the most follows 'A' OR 'B'? ").lower()
    check = is_higher(user_input,ran1['follower_count'],ran2['follower_count'])
    if check:
        print("Thats right")
        score += 1
    else:
        play = False
        print(f"nice try but that was wrong, your score is: {score}")