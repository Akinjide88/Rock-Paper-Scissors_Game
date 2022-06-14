import random
options = ["R", "P", "S"]
cpu = random.choice(options)
player_score = 0
cpu_score = 0
player = False

opt = """
R for rock
P for paper
S for scissors
"""

while True:

    print(opt)
    player = input("Pick an option between R, P or S\n").capitalize()
    
    if player == cpu:
        print("Ties!")
    
    elif player == "R":
        if cpu == "P":
            print("You lose!", cpu, "covers", player)
            print(f"Player {player} : CPU {cpu}")
            cpu_score+=1
            
        else:
            print("You win!", player, "smashes", cpu)
            print(f"Player {player} : CPU {cpu}")
            player_score+=1
    
    elif player == "P":
        if cpu == "S":
            print("You lose!", cpu, "cut", player)
            print(f"Player {player} : CPU {cpu}")
            cpu_score+=1
        
        else:
            print("You win!", player, "covers", cpu)
            print(f"Player {player} : CPU {cpu}")
            player_score+=1

    elif player == "S":
        if cpu == "R":
            print("You lose!", cpu, "smashes", player)
            print(f"Player {player} : CPU {cpu}")
            cpu_score+=1
        else:
            print("You win!", player, "cut", cpu)
            print(f"Player {player} : CPU {cpu}")
            player_score+=1
            
    elif player == "End":
        print("Final Score")
        print(f"Player {player_score} : CPU {cpu_score}")
        break