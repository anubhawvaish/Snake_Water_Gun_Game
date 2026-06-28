import random

print("===== Snake Water Gun Game =====")
print("Choices:")
print("s = Snake")
print("w = Water")
print("g = Gun")

computer_score = 0
user_score = 0

choices = ["s", "w", "g"]

for round in range(1, 6):
    print(f"\n----- Round {round} -----")

    computer = random.choice(choices)
    user = input("Enter your choice (s/w/g): ").lower()

    if user not in choices:
        print("Invalid Choice!")
        continue

    print("Computer chose:", computer)

    if user == computer:
        print("It's a Draw!")

    elif user == "s" and computer == "w":
        print("You Win! Snake drinks Water.")
        user_score += 1

    elif user == "w" and computer == "g":
        print("You Win! Water damages Gun.")
        user_score += 1

    elif user == "g" and computer == "s":
        print("You Win! Gun kills Snake.")
        user_score += 1

    else:
        print("Computer Wins!")
        computer_score += 1

    print(f"Score -> You: {user_score} | Computer: {computer_score}")

print("\n===== Final Result =====")

print(f"Your Score: {user_score}")
print(f"Computer Score: {computer_score}")

if user_score > computer_score:
    print(" Congratulations! You won the game.")
elif computer_score > user_score:
    print("Computer won the game.")
else:
    print("is a draw.")