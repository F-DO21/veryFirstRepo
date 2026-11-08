
#Description: A rock-paper-scissors game with a twist. Like in a Tug of War, one must win until the mark is in either side.

def display_board(state):                                                                                                               # this function will display the score board.
    print("=====================================================\n")                                                                    # this is the header or divider per round.
    print(f"ROUNDS PLAYED: {state['rounds_played']}")                                                                                   # get rounds_played value and display it before the rope
    theRope = f"[P WIN] <-- [{' ]--[' * (3 + state['rope_position'])}X{']--[ ' * (3 - state["rope_position"])}] --> [C WIN]\n"          # the final dynamic rope: I don't know if this is the definitive version but it took me 6 iteration to figure this simple arithmetic I almost cried. 
    print(theRope)                                                                                                                      # display the dynamic rope relative the current round rope position.

    '''                                                                                                                                 # This is my fourth iteration of the display board. I can't understand what was meant about 'dynamically display' so I proceed with this unti I read the instruction again saying 'using string replication' and remebering the * operator.
    theRope = "[P WIN] <-- [ ]--[ ]--[ ]--[ ]--[ ]--[ ]--[ ] --> [C WIN]\n"                                                             # (I just really want to share my initial thought process) this line is the initial string.
    divideRope = list(theRope)                                                                                                          # convert the string to a list of individual char, making it accessible and editable per index.
    divideRope[28 + (state["rope_position"] * 5)] = "X"                                                                                 # figured out a mathematical equation to replace a whitespace with the "X" mark)
    theRope = "".join(divideRope)                                                                                                       # join the list back to a single string.
    print(theRope)                                                                                                                      # display the edited string with the X.
    '''

def get_player_choice():                                                                                                                # this will get the player input.
    try:                                                                                                                                # to test for any error.
        choice = input("Choose your weapon! [R]ock, [P]aper, or [S]cissors: ").strip().upper()                                          # user input and assigned to the variable, stripped with whitespaces and coverted to uppercase.
        RPS = ["R", "P", "S"]                                                                                                           # this made me crazy! I previously used if-elif-else, and because of that, I can't make it throw any error because inputs are strings and the else "catch 'em all" errors. So I converted it to list.
        return RPS.index(choice)                                                                                                        # and accessing the list's index to return integer 0-2 while any invalid input will trigger the except catching ValueError.
    except ValueError:                                                                                                                  # ValueError catcher.
        print("[!] INVALID CHOICE: Please enter R, P, or S.\n")                                                                         # print the error msg.
        return 404                                                                                                                      # return a value that will signal an error.

def evaluate_round(player, computer, state):                                                                                            # the game logic: I used tuples here.
    if (player, computer) in [(0, 1), (1, 2), (2, 0)]:                                                                                  # COMP WON: getting player and comp input and if it is IN the list of tuples, then computer won the round.
        state["rope_position"] += 1                                                                                                     # then, the rope position value in the dictionary adds 1, so we can you use it in the display.
        return "Computer WINS this round! It tugs the rope right!"                                                                      # display computer wins the round.
    elif (player, computer) in [(0, 2), (1, 0), (2, 1)]:                                                                                # PLAYER WON: after player and comp input, if it is IN the list of tuples here, then player won the round.
        state["rope_position"] -= 1                                                                                                     # the rope position value subtracts 1,
        return "You WIN this round! You tug the rope left!"                                                                             # and announce player won.
    if player == computer:                                                                                                              # if player input is the same as computer,
        return "It's a TIE! The rope stands still."                                                                                     # just print a tie msg, nothing else to edit.

def main():                                                                                                                             # the main function ...
    import random                                                                                                                       # import the built-in random module.
    print("=====================================================\n            RPS TUG-OF-WAR (VS. COMPUTER)            ")               # prints the header and the title. Noticed the lower part is missing? It's on display_board() acting as the round divider.
    game_state ={"rope_position": 0, "win_threshold": -3, "loss_threshold": 3, "rounds_played": 0}                                      # the game state dictionary where the rope position, thresholds, and rounds count is kept.
    while True:                                                                                                                         # while valid, game will loop
        display_board(game_state)                                                                                                       # call the function display_board() to its thing.
        if game_state["rope_position"] == game_state["win_threshold"]:                                                                  # check if the rope position is equal to the win threshold in the dict,
            print("CONGRATULATIONS! You pulled the computer into your zone and WON the match!")                                         # print msg congratulating you.
            break                                                                                                                       # end the game.                                                                       
        elif game_state["rope_position"] == game_state["loss_threshold"]:                                                               # check if rope position is equal to the loss threshold,
            print("You lost! Better luck next time ( ͡° ͜ʖ ͡°).")                                                                          # print loss msg.
            break                                                                                                                       # end the game.
        else:                                                                                                                           # but if the thresholds are not yet met,
            player = get_player_choice()                                                                                                # get player input
            if player == 404:                                                                                                           # if it return other than 0, 1, or 2,
                game_state["rope_position"] += 1                                                                                        # automatic lost for the current round
                result = "Foul play! Computer pulls the rope right while you are distracted!"                                           # dispalying a warning of foul play.
            else:                                                                                                                       # but if player returns 0, 1, or 2,
                computer = random.randint(0, 2)                                                                                         # computer will get a random integer from 0 to 2.
                RPS = ["R", "P", "S"]                                                                                                   # a list for the computer.
                print(f"\n>> You threw: {RPS[player]}")                                                                                 # print player pick.
                print(f">> Computer threw: {RPS[computer]}")                                                                            # print computer pick.
                result = evaluate_round(player, computer, game_state)                                                                   # insert them to evaluate_round() function
            print(f">> RESULT: {result}\n")                                                                                             # and print the result of the round
        game_state["rounds_played"] += 1                                                                                                # then increment the rounds played at the end of a round.

if __name__ == "__main__":                                                                                                              # condition to not accidenttally run the program if ever imported.
    main()                                                                                                                              # start the main() program.