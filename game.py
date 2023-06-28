import random

player = {
    "name": "player",
    "HP": 20,
    "SP": 30,
    "AT": 5
}

enemy = {
    "name": "enemy",
    "HP": 30,
    "SP": 25,
    "AT": 8
}

def enemy_choice():
    nextATK = ""

    if enemy["SP"] <= 0:
        nextATK = "exhausted"
        return nextATK

    num = random.randrange(1,3)
    # print(num)
    if enemy["SP"] < 10:
        nextATK = "rest"
    elif num == 2:
        nextATK = "heavyATK"
    else:
        nextATK = "lightATK"
    
    return nextATK

def enemy_warning(choice):
    if choice == "lightATK":
        text = "Your opponent swiftly readies their weapon, lifting it up to their right side and prepares to swing."
    elif choice == "heavyATK":
        text = "Your opponent lifts their weapon high above their head preparing to cleave down at you with full force."
    elif choice == "rest":
        text = "Your opponent pants heavily as they attempt to catch their breath."
    elif choice == "exhausted":
        text = "Your opponent is out of energy. They drop their guard and pant heavily as they desperately attempt to catch their breath."

    return text

def move_comparison(enemyM, playerM):
    if enemyM == "exhausted" and playerM == "finish":
        player["SP"] -= 4
        enemy["HP"] = 0
        return "You take advantage of your opponents' exaustion and bury your blade into their chest, finishing them off."
    elif enemyM == "exhausted" and playerM == "attack":
        player["SP"] -= 4
        enemy["SP"] += 6
        enemy["HP"] -= player["AT"]
        return "You take advantage of the enemies break and strike them."
    elif enemyM == "exhausted" and playerM == "rest":
        player["SP"] += 12
        enemy["SP"] += 10
        return "Seeing that your opponent is winded, you take a moment to catch your breath as well."
    elif enemyM == "rest" and playerM == "evade":
        player["SP"] -= 6
        enemy["SP"] += 10
        return "You dodge nothing as your opponent desperately recovers."
    elif enemyM == "rest" and playerM == "block":
        player["SP"] += 8
        enemy["SP"] += 10
        return "You hold your sword up in fear, but nothing happens. Your opponent instead attempts to desperately recover."
    
    if enemyM == "lightATK" and playerM == "block":
        player["SP"] -= 4
        enemy["SP"] -= 8
        return "You successfully block the attack."
    elif enemyM == "lightATK" and playerM != "block":
        player["HP"] -= enemy["AT"]
        enemy["SP"] -= 4
        return "The enemy's attack is too fast and you're struck."
    
    if enemyM == "heavyATK" and playerM == "evade":
        player["SP"] -= 6
        enemy["SP"] -= 10
        return "The slow attack is easily avoided."
    elif enemyM == "heavyATK" and playerM != "evade":
        player["HP"] -= (enemy["AT"] * 1.5)
        enemy["SP"] -= 6
        return "The attack is powerful and because you didn't move you were struck with a crushing blow."
    
    if enemyM == "rest" and playerM == "attack":
        player["SP"] -= 4
        enemy["SP"] += 6
        enemy["HP"] -= player["AT"]
        return "You take advantage of the enemies break and strike them."
    elif enemyM == "rest" and playerM == "rest":
        player["SP"] += 12
        enemy["SP"] += 10
        return "Seeing that your opponent is taking a break, you take a moment to catch your breath as well."
    elif enemyM == "rest" and playerM == "evade":
        player["SP"] -= 6
        enemy["SP"] += 10
        return "You dodge nothing as your opponent takes a breather and recovers some energy."
    elif enemyM == "rest" and playerM == "block":
        player["SP"] += 8
        enemy["SP"] += 10
        return "You hold your sword up in fear, but nothing happens. Your opponent catches their breath and you do too a bit."
    elif enemyM == "rest" and playerM == "kick":
        player["SP"] -= 5
        enemy["HP"] -= 2
        enemy["SP"] -= 8
    

def fight():
    enemy_move = enemy_choice()
    enemy_text = enemy_warning(enemy_move)
    print("-------------------------------------------")
    print(enemy_text)
    print("-------------------------------------------")
    player_move = input("What do you do? ")
    print("-------------------------------------------")
    result = move_comparison(enemy_move, player_move)
    print(result)
    print("-------------------------------------------")
    print(f"Player: HP = {player['HP']} SP = {player['SP']}")
    print(f"Enemy: HP = {enemy['HP']} SP = {enemy['SP']}")

while enemy["HP"] > 0 and player["HP"] > 0:
    fight()
print("-------------------------------------------")
if player["HP"] <= 0:
    print("You have died...")
elif enemy["HP"] <= 0:
    print("You were victorious!")
print("-------------------------------------------")
print("GAME END")