from agents.router_agent import route_task

def main():
    print("\n🧠 report-writer agent CLI")
    print("--------------------------")

    while True:
        print("\nAvailable commands:")
        print("  plan   → generate spec/blueprint")
        print("  code   → implement pipeline functions")
        print("  test   → generate unit tests from plan")
        print("  review → audit test logic")
        print("  quit   → exit\n")

        cmd = input("Enter command: ").strip().lower()

        if cmd in {"quit", "exit"}:
            break
        elif cmd in {"plan", "code", "test", "review"}:
            result = route_task(cmd)
            print(f"\n{result}\n")
        else:
            print("❌ Invalid command")

if __name__ == "__main__":
    main()
