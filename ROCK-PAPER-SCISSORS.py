import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_user_choice():
    while True:
        choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if choice in ["rock", "paper", "scissors"]:
            return choice
        print("❌ Invalid input. Try again.")

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    wins = {"rock": "scissors", "scissors": "paper", "paper": "rock"}
    return "user" if wins[user] == computer else "computer"

def main():
    print("🎮 Welcome to Rock-Paper-Scissors!")
    user_score = computer_score = round_num = 0

    while True:
        round_num += 1
        print(f"\n🔁 Round {round_num}")
        user = get_user_choice()
        comp = get_computer_choice()

        print(f"🧑 You: {user} | 💻 Computer: {comp}")
        result = determine_winner(user, comp)

        if result == "tie":
            print("🤝 It's a tie!")
        elif result == "user":
            print("✅ You win this round!")
            user_score += 1
        else:
            print("❌ Computer wins this round!")
            computer_score += 1

        print(f"📊 Score => You: {user_score} | Computer: {computer_score}")

        if input("\nPlay again? (yes/no): ").lower() != "yes":
            print("\n🏁 Game Over!")
            print(f"Final Score => You: {user_score} | Computer: {computer_score}")
            if user_score > computer_score:
                print("🎉 You won the game!")
            elif user_score < computer_score:
                print("😔 Computer won the game.")
            else:
                print("🤝 It's a draw!")
            break

if __name__ == "__main__":
    main()
