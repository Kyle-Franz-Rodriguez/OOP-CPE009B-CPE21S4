from Novice import Novice
from Swordsman import Swordsman
from Archer import Archer
from Mage import Mage
from Boss import Boss
from Monster import Monster
import random
import time

def novice_battle(player, enemy):
    turn = 0
    while player.getHp() > 0 and enemy.getHp() > 0:
        turn += 1
        print('')
        time.sleep(1) 
        print(f"\nRound {turn}:")
        print("************************************")
        print(f"!----{enemy.getUsername()} - HP: {enemy.getHp()}----!")
        print(f"{player.getUsername()} - HP: {player.getHp()}")
        print("************************************")
        time.sleep(1)
        #Random turns
        if random.randint(0, 1) == 0:
            print("\nWhat would you like to do?\n[1] Basic attack")
            attack = input('- ')
            if attack == '1':
                player.basicAttack(enemy)
                time.sleep(1) 
            else:
                print("-<You stood still not knowing what to do>-")
                time.sleep(1)
        else:
            print(f"-<{enemy.getUsername()}'s turn>-")
            time.sleep(1)
            if random.randint(0, 3) == 0:
                enemy.basicAttack(player)
                time.sleep(1) 
            elif random.randint(0, 3) == 1: 
                enemy.slashAttack(player)
                time.sleep(1)
            elif random.randint(0, 3) == 2:
                enemy.rangedAttack(player)
                time.sleep(1)
            else:
                enemy.magicAttack(player)
                time.sleep(1)

    if player.getHp() > 0:
        time.sleep(2) 
        print("************************************")
        print(f"{player.getUsername()} has won the battle!")
        print("************************************")
        return 1
    else:
        time.sleep(2) 
        print(f"{enemy.getUsername()} has won the battle!")
        return 0

def swordsman_battle(player, enemy):
    turn = 0
    while player.getHp() > 0 and enemy.getHp() > 0:
        turn += 1
        print('')
        time.sleep(1) 
        print(f"\nRound {turn}:")
        print("************************************")
        print(f"!----{enemy.getUsername()} - HP: {enemy.getHp()}----!")
        print(f"{player.getUsername()} - HP: {player.getHp()}")
        print("************************************")
        time.sleep(1)
        #Random turns
        if random.randint(0, 1) == 0:
            print("\nWhat would you like to do?\n[1] Basic attack\n[2] Slash Attack")
            attack = input('- ')
            if attack == '1':
                player.basicAttack(enemy)
                time.sleep(1) 
            elif attack == '2':
                player.slashAttack(enemy)
                time.sleep(1)
            else:
                print("-<You stood still not knowing what to do>-")
                time.sleep(1)
        else:
            print(f"-<{enemy.getUsername()}'s turn>-")
            time.sleep(1)
            if random.randint(0, 3) == 0:
                enemy.basicAttack(player)
                time.sleep(1) 
            elif random.randint(0, 3) == 1: 
                enemy.slashAttack(player)
                time.sleep(1)
            elif random.randint(0, 3) == 2:
                enemy.rangedAttack(player)
                time.sleep(1)
            else:
                enemy.magicAttack(player)
                time.sleep(1)

    if player.getHp() > 0:
        time.sleep(1) 
        print("************************************")
        print(f"{player.getUsername()} has won the battle!")
        print("************************************")
        return 1
    else:
        time.sleep(2) 
        print('')
        print(f"{enemy.getUsername()} has won the battle!")
        return 0

def archer_battle(player, enemy):
    turn = 0
    while player.getHp() > 0 and enemy.getHp() > 0:
        turn += 1
        print('')
        time.sleep(1) 
        print(f"\nRound {turn}:")
        print("************************************")
        print(f"!----{enemy.getUsername()} - HP: {enemy.getHp()}----!")
        print(f"{player.getUsername()} - HP: {player.getHp()}")
        print("************************************")
        time.sleep(1)
        #Random turns
        if random.randint(0, 1) == 0:
            print("\nWhat would you like to do?\n[1] Basic attack\n[2] Ranged Attack")
            attack = input('- ')
            if attack == '1':
                player.basicAttack(enemy)
                time.sleep(1) 
            elif attack == '2': 
                player.rangedAttack(enemy)
                time.sleep(1)                
            else:
                print("-<You stood still not knowing what to do>-")
                time.sleep(1)
        else:
            print(f"-<{enemy.getUsername()}'s turn>-")
            time.sleep(1)
            if random.randint(0, 3) == 0:
                enemy.basicAttack(player)
                time.sleep(1) 
            elif random.randint(0, 3) == 1: 
                enemy.slashAttack(player)
                time.sleep(1)
            elif random.randint(0, 3) == 2:
                enemy.rangedAttack(player)
                time.sleep(1)
            else:
                enemy.magicAttack(player)
                time.sleep(1)

    if player.getHp() > 0:
        time.sleep(2) 
        print("************************************")
        print(f"{player.getUsername()} has won the battle!")
        print("************************************")
        return 1
    else:
        time.sleep(2) 
        print(f"{enemy.getUsername()} has won the battle!")
        return 0

def mage_battle(player, enemy):
    turn = 0
    while player.getHp() > 0 and enemy.getHp() > 0:
        turn += 1
        print('')
        time.sleep(1) 
        print(f"\nRound {turn}:")
        print("************************************")
        print(f"!----{enemy.getUsername()} - HP: {enemy.getHp()}----!")
        print(f"{player.getUsername()} - HP: {player.getHp()}")
        print("************************************")
        time.sleep(1)
        #Random turns
        if random.randint(0, 1) == 0:
            print("\nWhat would you like to do?\n[1] Basic attack\n[2] Magic Attack\n[3] Heal")
            attack = input('- ')
            if attack == '1':
                player.basicAttack(enemy)
                time.sleep(1) 
            elif attack == '2':
                player.slashAttack(enemy)
                time.sleep(1)
            elif attack == '3':
                player.heal()
                time.sleep(1)
            else:
                print("-<You stood still not knowing what to do>-")
                time.sleep(1)
        else:
            print(f"-<{enemy.getUsername()}'s turn>-")
            time.sleep(1)
            if random.randint(0, 3) == 0:
                enemy.basicAttack(player)
                time.sleep(1) 
            elif random.randint(0, 3) == 1: 
                enemy.slashAttack(player)
                time.sleep(1)
            elif random.randint(0, 3) == 2:
                enemy.rangedAttack(player)
                time.sleep(1)
            else:
                enemy.magicAttack(player)
                time.sleep(1)

    if player.getHp() > 0:
        time.sleep(2) 
        print("************************************")
        print(f"{player.getUsername()} has won the battle!")
        print("************************************")
        return 1
    else:
        time.sleep(2) 
        print(f"{enemy.getUsername()} has won the battle!")
        return 0

def pvp_battle(p1, p2):
    print("************************************")
    print(f"!----{p1.getUsername()} - HP: {p1.getHp()}----!")
    print(f"!----{p2.getUsername()} - HP: {p2.getHp()}----!")
    print("************************************")

#DRIVER ----------------------------------------------------------------------
print ("!!!!----!!!!BATTLEFIELD!!!!----!!!!")
print('')
print("press [1] to start \n\n")
starter =input("- ")
print('')

if starter == '1':
    while starter == '1':
        print("Select your Gamde Mode: ")
        print("[1] Single-player Battle")
        print("[2] Multiplayer PVP")
        print("press any key to exit")
        print("\n")
        
        modeselect = input("- ")
        if modeselect == '1':
            counter = 0
            #NOVICE FIGHT
            
            print("-<You entered the battlefield alone>-")
            print("Enter a name for your charaacter")
            username = input("- ")
            character1 = Novice(username)
            print(f"You've set your name to {character1.getUsername()}\n\n")
            time.sleep(2)
            noviceloop = True
            while counter != 2 or noviceloop:
                monster1 = Monster("Monster")
                print("!!----!!A monster appeared!!----!!")
                counter += novice_battle(character1, monster1)
                time.sleep(1)
                print("Wins:", counter)
                print("\n[1] Continue fighting?\n")
                nextbattle = input("- ")
                if nextbattle == '1':
                    print("-<You continued to fight>-")
                    time.sleep(1)
                else:
                    noviceloop = False
                    break

            #SELECTING CLASS
            if counter == 2:
                time.sleep(1)
                print("You finished 2 battles. You can now select your class")
                print("!Selecting classes presents a new skill!")
                print("[1] Swordsman. Get skill <Slash Attack>")
                print("[2] Archer. Get skill <Ranged Attack>")
                print("[3] Mage. Get skill <Heal> <Magic Attack>")
                print("[Any] To exit")
                class_choice = input("- ")
                loop = True
                #BATTLES
                #Swordsman class
                if class_choice == '1':
                    character1 = Swordsman(username)
                    print("You've set your class to <Swordsman>")
                    wins = 0
                    while loop:
                        time.sleep(2)
                        monster1 = Boss("Monster")
                        print("!!----!!A monster appeared!!----!!")
                        wins += swordsman_battle(character1, monster1)
                        time.sleep(1)
                        print("Wins:", wins)
                        print("\n[1] Continue fighting?\n")
                        nextbattle = input("- ")
                        if nextbattle == '1':
                            print("-<You continued to fight>-")
                            time.sleep(1)
                        else:
                            loop = False
                               
                #Archer class
                elif class_choice == '2':
                    character1 = Archer(username)
                    print("You've set your class to <Archer>")
                    wins = 0
                    while loop:
                        time.sleep(2)
                        monster1 = Boss("Monster")
                        print("!!----!!A monster appeared!!----!!")
                        wins += archer_battle(character1, monster1)
                        time.sleep(1)
                        print("Wins:", wins)
                        print("\n[1] Continue fighting?\n")
                        nextbattle = input("- ")
                        if nextbattle == '1':
                            print("-<You continued to fight>-")
                            time.sleep(1)
                        else:
                            loop = False
                
                #Mage class
                elif class_choice == '3':
                    character1 = Mage(username)
                    print("You've set your class to <Mage>")
                    wins = 0
                    while loop:
                        time.sleep(2)
                        monster1 = Boss("Monster")
                        print("!!----!!A monster appeared!!----!!")
                        wins += mage_battle(character1, monster1)
                        time.sleep(1)
                        print("Wins:", wins)
                        print("\n[1] Continue fighting?\n")
                        nextbattle = input("- ")
                        if nextbattle == '1':
                            print("-<You continued to fight>-")
                            time.sleep(1)
                        else:
                            loop = False

                else:
                    time.sleep(1)
                    loop = False
                
        elif modeselect == '2':
            print("Selected <PVP>")
            
            print("Set a name for player 1: ")
            name1 = input('- ')
            player1 = Novice(name1)
            print(f"Set a class for {player1.getUsername()}")
            print("[1] Swordsman. Get skill <Slash Attack>")
            print("[2] Archer. Get skill <Ranged Attack>")
            print("[3] Mage. Get skill <Heal> <Magic Attack>")
            print("[Any] To exit")
            player1_class = input("- ")
            if player1_class == '1':
                player1 = Swordsman(name1)
            elif player1_class == '2':
                player1 = Archer(name1)
            elif player1_class == '3':
                player1 = Mage(name1)
            else:
                print("Class creation cancelled by {player1.getUsername()}")
           
            print("Set a name for player 2: ")
            name2 = input('- ')
            player2 = Novice(name2)
            print(f"Set a class for {player2.getUsername()}")
            print("[1] Swordsman. Get skill <Slash Attack>")
            print("[2] Archer. Get skill <Ranged Attack>")
            print("[3] Mage. Get skill <Heal> <Magic Attack>")
            print("[Any] To exit")
            player2_class = input("- ")
            if player2_class == '1':
                player2 = Swordsman(name2)
            elif player2_class == '2':
                player2 = Archer(name2)
            elif player2_class == '3':
                player2 = Mage(name2)
            else:
                print("Class creation cancelled by {player2.getUsername()}")
            
            pvp_battle(player1, player2)
            
            
        else:
            print("---Exiting---")
            starter = 0
