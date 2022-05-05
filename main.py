# This is program is to prove my math teacher wrong

from random import randint

player_won = 0
player_lost = 0
numbers_of_matches_lost = 0

numbers_of_matches = int(input("Choose how many matches you want to simulate "))

for _ in range(numbers_of_matches):
    car_is = opened_door = randint(1, 3) # The door that opens will be based on where the car is
    player_choice = randint(1, 3)
    
    while opened_door in (car_is, player_choice):
        opened_door = randint(1, 3)
        
    if (player_choice == 2 and opened_door == 3) or (player_choice == 3 and opened_door == 2):
        player_choice = 1
    elif (player_choice == 1 and opened_door == 3) or (player_choice == 3 and opened_door == 1):
        player_choice = 2
    elif (player_choice == 1 and opened_door == 2) or (player_choice == 2 and opened_door == 1):
        player_choice = 3
                
    if player_choice == car_is:
        player_won += 1
    if player_choice != car_is:
        player_lost += 1

        numbers_of_matches_lost = numbers_of_matches - player_won
        print(f"You won and your score is now {player_won} to {player_lost} matches lost")

print()
print(f"You have done {numbers_of_matches} matches.")
print(f"You lost {player_lost} times, which is loosing {(player_lost/numbers_of_matches*100):.1f}% of the matches")
print(f"You have you won {player_won} times, which is winning {(player_won/numbers_of_matches*100):.1f}% of the matches")
