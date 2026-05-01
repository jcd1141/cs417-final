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

def group_by_position(players):  #Groups players by position
    positions = {}  #Dictionary where each position will have its own list

    for player in players:  
        position = player["position"]  #Get player's position

        if position not in positions: 
            positions[position] = []  

        positions[position].append(player)  #Add player to the correct position list

    return positions

def build_heap(players):  #Creates a heap to rank players by projected points
    heap = []

    for player in players:
        projected = player["projected"]  
        name = player["name"] 

        heapq.heappush(heap, (-projected, name, player))

    return heap 

def get_best_player(players):  #Returns the highest projected player
    if len(players) == 0:
        return None

    heap = build_heap(players) 
    best = heapq.heappop(heap)[2]  

    return best

def main():
    starters = load_players("data/roster.csv") #Loading players
    bench = load_players("data/bench.csv")
    free_agents = load_players("data/free_agents.csv")

    all_players = starters + bench + free_agents #Puts all players into one list
    grouped = group_by_position(all_players) #Positions grouped

    for position in grouped: #Testing best
        best = get_best_player(grouped[position])
        print(position, "BEST:", best["name"], "-", best["projected"])

if __name__ == "__main__":
    main()