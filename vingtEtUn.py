# Juan Reyes
# vingtEtUn.py
# April 26 2023
#
# This program runs the game "Vingt-et-un" (Blackjack).
# A menu-driven UI will be present, displaying options
# for the rules, the game itself, or to quit the
# program. When running the game, the player (user) will
# play against the house (program) to win. The results
# will display at the end of the game.
#
# Input: 1. Name of the player
#        2. A number (1-3)
#        3. A letter (S/R)
#
# Processing: 1. Prompt user for player name
#             2. Prompt user to pick options 1-3
#             3. When running the game (option 2):
#               - Go into a loop of rounds where player & house
#                 will take turns throwing the dice.
#               - Prompt player to stay or roll
#                   * If house total is >= 17, it stays and turn
#                     passes to the player
#               - Simulate roll of two dice and update player's
#                 total
#                   * If player/house total is >= 14, only one dice
#                     will be rolled.
#               - Determine results once game is over
#             4. Prompt user with options until user quits the program
#
# Output: 1. Display rules of the game when option 1 is selected
#         2. Run the game when option 2 is selected
#           - Display player's/house's accumulated total during
#             the game
#           - Display results of the game (who won and who lost the
#             game, or if the game ended in a tie)
#         3. Display a good-bye message and quit when option 3 is selected

# Import modules
import random

print('Welcome to Vingt-et-un!')
# Prompt user for player name
playerName = input('Please enter your name: ')

# Main function
def main():
    # Initialize control variable
    menu = 0

    while menu != 3:
        # Display menu options
        print("-"*22)
        print("Vingt-et-un Game Menu\
               \n1. See the rules.\
               \n2. Play Vingt-et-un.\
               \n3. Quit.")
        # Prompt user to select an option
        menu = int(input("\nPlease select an option (1-3): "))

        # Show rules
        if menu == 1:
            showRules()

        # Start game
        elif menu == 2:
            playGame()

        # Quit program
        elif menu == 3:
            # Goodbye message
            print('\nGoodbye. Thank you for playing Vingt-et-un.')

        # Input validation
        else:
            print('\nError ... Invalid option. Try Again.')

#
# showRules()
#
# Displays the rules of Vingt-et-un
#
def showRules():
    print("\nVingt-et-un is a dice game (known as Blackjack in the USA)\
           \nwhere a player competes against the computer (house).\
           \n\
           \nThe goal of the game is to score 21 points or as near as\
           \npossible without going over. The two players take turns\
           \nthrowing two die as many times as desired and adding up\
           \nthe numbers thrown on each round.\
           \n\
           \n-> A player who totals over 21 is bust and loses the game.\
           \n-> The player whose total is nearest 21, after each player\
           \nhas had a turn, wins the game.\
           \n-> In the case of an equally high total, the game is tied.\
           \n\
           \nThe game is over at the end of a round when:\
           \n\
           \n-> One or both players are bust.\
           \n-> Both players choose to stay.\
           \n\
           \nThings to Take Note:\
           \n-> Once a player totals 14 or more, one of the dice is\
           \ndiscarded for the consecutive turns.\
           \n-> The house must throw the dice until the total is 17 or\
           \nhigher. At 17 or higher, the house must stay.")

#
# rollDice()
#
# Simulates the roll of the dice and
# displays their result
#
def rollDice():
    return random.randint(1,6)

#
# playGame()
#
# Runs the game, including player and
# house turns, calculating the running
# totals, and determining the winner.
#
def playGame():
    playerTotal = 0
    houseTotal = 0
    gameOver = False

    while not gameOver:
        # Player's turn
        print(f"\n{playerName}'s turn.")
        playerChoice = input("Do you want to stay or roll? (s/r): ")
        
        if playerChoice == 's':
            print('\nYou chose to stay.')

        elif playerChoice == "r":

            # Only one die is rolled
            if playerTotal >= 14 and playerTotal <= 21:
                print('\nOnly one die will be rolled.')
                playerTotal += rollDice()
                print(f"{playerName}'s total:", str(playerTotal))

            # Both dice are rolled     
            elif playerTotal < 14:
                print('\nTwo dice will be rolled.')
                playerTotal += rollDice() + rollDice()
                print(f"{playerName}'s total:", str(playerTotal))

            elif playerTotal > 21:
                print(f"\n{playerName} is bust.")
                gameOver = True
                break
        
        # Input validation
        else:
            print("\nPlease enter either s or r.")

        # House's turn
        print("\nHouse's turn.")        
        if houseTotal >= 17:
            print("House's total:", str(houseTotal))
            break

        elif houseTotal >= 14 and houseTotal <= 21:
                print('Only one die will be rolled.')
                houseTotal += rollDice()
                print("House's total:", str(houseTotal))
        
        elif houseTotal < 14:
            print('Two dice will be rolled.')
            houseTotal += rollDice() + rollDice()
            print("House's total:", str(houseTotal))

        elif houseTotal > 21:
            print("\nHouse is bust.")
            gameOver = True
            break
        
    # Both players are bust
    if playerTotal > 21 and houseTotal > 21:
        print('Both players are bust. No one wins.')

    # Player is bust
    elif playerTotal > 21:
        print("\nHouse wins.")
        
    # House is bust
    elif houseTotal > 21:
        print(f"\n{playerName} wins.")
        
    # Player and House tie
    elif playerTotal == houseTotal:
        print("\nIt's a tie.")
        
    # Player wins, House loses
    elif playerTotal > houseTotal:
        print(f"\n{playerName} wins.")
        
    # House wins, Player loses
    elif playerTotal < houseTotal:
        print("\nHouse wins.")

# Run main function
if __name__ == '__main__':
    main()
