from logic import load_players
from logic import print_players
from logic import recommend_starter_changes
from logic import recommend_bench_changes


def main():
    starters = load_players("data/roster.csv", "starter")
    bench = load_players("data/bench.csv", "bench")
    free_agents = load_players("data/free_agents.csv", "free agency")

    while True:
        print()
        print("Fantasy Football Optimizer")
        print("--------------------------")
        print("1. Show Starters")
        print("2. Show Bench")
        print("3. Show Free agents")
        print("4. Optimize Starters")
        print("5. Optimize Bench")
        print("6. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            print_players("Starters", starters)

        elif choice == "2":
            print_players("Bench", bench)

        elif choice == "3":
            print_players("Free Agents", free_agents)

        elif choice == "4":
            recommend_starter_changes(starters, bench, free_agents)

        elif choice == "5":
            recommend_bench_changes(bench, free_agents)

        elif choice == "6":
            print("Goodbye.")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()