from logic import load_players
from logic import recommend_changes

def main():
    starters = load_players("data/roster.csv")
    bench = load_players("data/bench.csv")
    free_agents = load_players("data/free_agents.csv")

    recommend_changes(starters, bench, free_agents)

if __name__ == "__main__":
    main()