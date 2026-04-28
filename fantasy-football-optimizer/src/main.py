import csv

def load_players(filename): #This is to load the players from CSV
    players = []

    file = open(filename, "r", encoding="utf-8")
    reader = csv.DictReader(file)

    for row in reader:
        player = {}

        player["name"] = row["name"]
        player["position"] = row["position"]
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

def main():
    starters = load_players("roster.csv") #Loading players
    bench = load_players("bench.csv")
    free_agents = load_players("free_agents.csv")

    print_players("Starters", starters) #Printing players
    print_players("Bench", bench)
    print_players("Free Agents", free_agents)

if __name__ == "__main__":
    main()