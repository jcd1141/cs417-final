Description:
This project is a command-line fantasy football optimizer. It reads player data from CSV files for starters, bench players, and free agents, and compares them based on projected points per game. The program then recommends whether to keep a player or replace them with a better option at the same position.

How To Run It:
The free agents, starters, and bench are all set up. Just by entering python src/main.py into the bash the program will begin. It works through a menu system.

Data Structures and Algorithms:
This project uses a dictionary (hash table) to group players by position, which is implemented in the group_by_position() function in logic.py. It also uses a heap (priority queue) in the build_heap() and get_best_player() functions to efficiently find the highest projected player. The recommendation logic uses comparisons between players to determine whether a starter or bench player should be replaced, which acts as the main algorithm of the program.

What's Working and What's Not:
The program can load players from CSV files, groups them by position, and finds the best available players using a heap. It can recommend starter upgrades and bench upgrades, and the menu system allows the user to interact with the program easily. However, the program does not update the CSV files automatically when changes are recommended. It also does not support more detailed fantasy football rules like flex positions.

AI Usage:
I used ChatGPT for a lot of debugging. For example, when and if I recieved a logic error I didn't understand, I would ask it to find it for me and explain why that was happening. I also used it if I ever forgot certain syntaxes within the code. 