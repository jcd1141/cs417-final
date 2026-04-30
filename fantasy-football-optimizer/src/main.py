import csv
import heapq

def load_players(filename): #This is to load the players from CSV
    players = [] #Stores players as dictionaries

    file = open(filename, "r", encoding="utf-8")
    reader = csv.DictReader(file)

    for row in reader:
        player = {} 

        player["name"] = row["name"].strip()
        player["position"] = row["position"].strip()
        player["projected"] = float(row["projected"])
        players.append(player)

    file.close()

    return players

def print_players(title, players): #Prints the players
    print()
    print(title)
    print("-" * len(title))

    for player in players:
        print(player["name"], "-", player["position"], "-", player["projected"])

def group_by_position(players):  # groups players by position
    positions = {}  # dictionary where each position will have its own list

    for player in players:  
        position = player["position"]  # get player's position

        if position not in positions: 
            positions[position] = []  

        positions[position].append(player)  # add player to the correct position list

    return positions

def main():
    starters = load_players("data/roster.csv") #Loading players
    bench = load_players("data/bench.csv")
    free_agents = load_players("data/free_agents.csv")

    all_players = starters + bench + free_agents #Puts all players into one list
    grouped = group_by_position(all_players) #Positions grouped

    for position in grouped: #Testing grouping
        print()
        print(position)
        print("-------")

        for player in grouped[position]:
            print(player["name"], "-", player["projected"])

if __name__ == "__main__":
    main()