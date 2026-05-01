import csv
import heapq

def load_players(filename, source): #This is to load the players from CSV
    players = [] #Stores players as dictionaries

    file = open(filename, "r", encoding="utf-8")
    reader = csv.DictReader(file)

    for row in reader:
        player = {} 

        player["name"] = row["name"].strip()
        player["position"] = row["position"].strip()
        player["projected"] = float(row["projected"].strip())
        player["source"] = source
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

def recommend_changes(starters, bench, free_agents):
    starters_by_position = group_by_position(starters)
    bench_by_position = group_by_position(bench)
    free_agents_by_position = group_by_position(free_agents)

    print()
    print("Recommended Changes")
    print("-------------------")

    for position in starters_by_position:
        starter_list = starters_by_position[position]

        for starter in starter_list:
            print()
            print(position + ":")
            print("Current starter:", starter["name"], "-", starter["projected"])

            options = []  #Possible replacements

            if position in bench_by_position:
                options = options + bench_by_position[position]

            if position in free_agents_by_position:
                options = options + free_agents_by_position[position]
            
            best_option = get_best_player(options)

            if best_option is None:
                print("No bench or free agent options found.")

            elif best_option["projected"] > starter["projected"]:
                print(
                    "Replace",
                    starter["name"],
                    "with",
                    best_option["name"],
                    "from",
                    best_option["source"],
                    "-",
                    best_option["projected"]
                )

            else:
                print("Keep", starter["name"])

