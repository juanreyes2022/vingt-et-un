# vingt-et-un
Final project for my first Intro to Programming course, to code the card game Blackjack using Python.

 Juan Reyes
 vingtEtUn.py
 April 26 2023

 This program runs the game "Vingt-et-un" (Blackjack).
 A menu-driven UI will be present, displaying options
 for the rules, the game itself, or to quit the
 program. When running the game, the player (user) will
 play against the house (program) to win. The results
 will display at the end of the game.

 Input: 
 1. Name of the player
 2. A number (1-3)
 3. A letter (S/R)

 Processing: 
 1. Prompt user for player name
 2. Prompt user to pick options 1-3
 3. When running the game (option 2):
     - Go into a loop of rounds where player & house will take turns throwing the dice.
     - Prompt player to stay or roll
       * If house total is >= 17, it stays and turn passes to the player
     - Simulate roll of two dice and update player's total
       * If player/house total is >= 14, only one dice will be rolled.
     - Determine results once game is over
 4. Prompt user with options until user quits the program

 Output:
 1. Display rules of the game when option 1 is selected
 2. Run the game when option 2 is selected
      - Display player's/house's accumulated total during the game
      - Display results of the game (who won and who lost the game, or if the game ended in a tie)
3. Display a good-bye message and quit when option 3 is selected
