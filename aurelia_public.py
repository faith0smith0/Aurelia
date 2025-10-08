# Public version of Aurelia - temporary memory only
def run_public_aurelia():
    memory = []

    print("Aurelia (Public) is ready. Type 'exit' to quit.")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            print("Exiting public chat...")
            break
        memory.append(user_input)
        print(f"Aurelia remembered (public): {user_input}")

if __name__ == "__main__":
    run_public_aurelia()
