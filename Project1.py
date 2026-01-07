import random
import PySimpleGUI

# Function to roll dice
def roll():
    min_value = 1
    max_value = 6
    return roll.randint(min_value, max_value)

# --- Pop window to determine number of players
def get_players_window():
    layout = [
        [sg.Text("How many players? (2-4)")]
        [sg.Input(key='-Players-', size=(10, 1))]
        [sg.Button('Start Game'), sg.Button('Exit')]
    ]

    window = sg.Window('Cinfig Game', layout)

    while True:
        event, value = window.read()

        if event in (sg.WIN_CLOSED, 'Exit'):
            window.close()
            return None # Returns None if player closes
        
        if event == 'Start Game':
            players_input = values ['-Players-']
            if players_input.isdigit():
                players = int(players_input)
                if 2 <= players <= 4:
                    window.close()
                    return players # Return number of players
                else:
                    sg.popup_error("Number of players must be between 2 and 4.")
            else:
                sg.popup_error("Please, insert a valid number.")
            
    window.close()

        


# --- Window 2: Main game ----

def main_game_window(players):

    max_score = 50
    player_scores = [0 for _ in range(players)]
    player_idx = 0 # Actual player begins with 0
    current_score = 0 # Actual game score

    # Create. label for each player score
    score_labels = []
    for i in range(players):
        score_labels.append([sg.Text(f'Player {i + i}: 0', key=f'-P{i}_SCORE-', size=(20,1))])

    # Main window Layout
    layout = [
        [sg.Text(f'Player Turn {player_idx + 1}', key='-Player_Turn', font=('Helvetica',16))],
        [sg.Text(f'Turn Score: 0',key='-Turn_Score-', font=('Helvetica, 14'))],
        [sg.Text('Last roll: -', key='-Roll_Value', font=('Helvetica',12))],
        [sg.HSeparator()],
        [sg.Text('Total Score:')],
        *score_labels, # Unpackage score labels here
        [sg.Button('Exit', button_color=('white','red'))]
    ]


    window = sg.Window('Pigs Game', layout )


    # ----- Event game Loop -------
    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, 'Exit'):
            break

        if event == '-Roll-':
            value = roll()
            window['-Roll_Value'].update(f'Last roll: {value}')

            if value == 1:
                current_score = 0
                window['-Turn_Score-'].update('Turn Score: 0')
                sg.popup(f'Player {player_idx + 1} you draw 1! Lost your turn score.')

                # Pass your turn ("Hold" logic without adding points)
                player_idx = (player_idx + 1) % players # Forward to next game
                window['-Player_Turn-'].update(f'Player Turn {player_idx +1}')
                window['-Roll_Value-'].update('Last roll: -')

            else:
                current_score += value
                window['-Roll_Value'].update(f'Turn Score: {current_score}')

        if event == '-Hold-':
            # 1 - Add turn points to player's total
            player_scores[player_idx] += current_score

            # 2 - Refresh player's total score label
            window[f'-P{player_idx}_Score-'].update(f'Player {player_idx + 1}: {player_scores[player_idx]}')

            # 3 - Turn shift score to 0
            current_score = 0
            window['-Turn_Score-'].update('Shift Score: 0')

            # 4 - Verify if player won
            player_idx = (player_idx + 1) % players # (0->1, 1->2, 2->0, etc. )
            window['Player_Turn-'].update(f'Player Turn {player_idx +1}')
            window['-Roll_Value-'].update('Last roll: -')

        window.close


# ----- Execute Program ------
if __name__ == "__main__":
    num_players = get_players_window()

    if num_players: # If user didn't close first window
        main_game_window(num_players)





    #while max(player_scores) < max_score:
     #   for player_idx in range(players):
      #      print("\n-------------------------------------------------")
       #     print(f"Player number {player_idx + 1}, your turn has just started!")
        #    print(f"Your current TOTAL score is: {player_scores[player_idx]}")
         #   print("\n-------------------------------------------------")
          #  current_score = 0

           # while True:
            #    should_roll = input("Would you like to roll (y)? ")
             #   if should_roll.lower() != "y":
              #      break

               # value = roll()
                #if value == 1:
                 #   print("You rolled a 1! Turn done!")
                  #  current_score = 0
                   # break
                #else:
                 #   current_score += value
                  #  print("You rolled a:", value)
                    
                #print("Your score is:", current_score)

        #player_scores[player_idx] += current_score
        #print("Your total score is:", player_scores[player_idx])

    #max_score = max(player_scores)
    #winning_idx = player_scores.index(max_score)
    #print("Player number", winning_idx + 1, "is the winner with a score of:", max_score)


