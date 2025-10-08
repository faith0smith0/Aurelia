memory_file = "aurelia_memory.txt"

def load_memory():
    try:
        with open(memory_file, "r") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return []

def save_memory(memories):
    with open(memory_file, "w") as f:
        f.write("\n".join(memories))

def view_memory(memories):
    if not memories:
        print("Memory is empty.")
    else:
        print("Aurelia's Memory:")
        for i, mem in enumerate(memories, 1):
            print(f"{i}: {mem}")

def add_memory(memories):
    new_mem = input("Enter new memory: ").strip()
    if new_mem:
        memories.append(new_mem)
        print(f"Added: {new_mem}")

def run_aurelia(memories):
    print("Aurelia is ready.")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting Aurelia chat...")
            break
        memories.append(user_input)
        print(f"Aurelia remembered: {user_input}")

def main():
    memories = load_memory()
    while True:
        print("\n--- Aurelia Control Menu ---")
        print("1. View memory")
        print("2. Add memory")
        print("3. Run Aurelia chat")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            view_memory(memories)
        elif choice == "2":
            add_memory(memories)
        elif choice == "3":
            run_aurelia(memories)
        elif choice == "4":
            save_memory(memories)
            print("Memory saved. Exiting controller.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
