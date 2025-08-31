import random
import matplotlib.pyplot as plt

questions = [
    ("What is the capital of India?", "Delhi"),
    ("2 + 2 = ?", "4"),
    ("What is the largest planet?", "Jupiter"),
    ("5 x 6 = ", "30"),
    ("What language is used for Android apps?", "Java"),
    ("12 / 4 = ?", "3"),
    ("H2O is commonly known as?", "Water"),
    ("Square root of 16?", "4"),
    ("Prime Minister of India (2025)?", "Narendra Modi"),
    ("What is 10^2?", "100")
]

def play_quiz(player_name):
    selected_indices = random.sample(range(len(questions)), 4)
    score = 0
    attempted = []
    print(f"\nQuiz Start for {player_name}!\n")
    for idx in selected_indices:
        q, ans = questions[idx]
        print(q)
        user_ans = input("Your answer: ").strip()
        attempted.append((q, user_ans, ans))
        if user_ans.lower() == ans.lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect! Correct Answer: {ans}\n")
    print(f"{player_name}, you got {score} out of 4 correct.\n")
    return score, attempted

def visualize_scores(score_data):
    names = [name for name, _, _ in score_data]
    scores = [score for _, score, _ in score_data]

    plt.figure(figsize=(8,6))
    bars = plt.bar(names, scores, color='skyblue')
    plt.xlabel("Player Name")
    plt.ylabel("Correct Answers (out of 4)")
    plt.title("Quiz Score Summary")
    for bar, score in zip(bars, scores):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(), str(score),
                 ha='center', va='bottom', fontweight='bold')
    plt.ylim(0,4.5)
    plt.tight_layout()
    plt.show()

def main():
    print("-" * 40)
    print("Welcome to the Quiz Game!")
    print("-" * 40)
    num_players = 0
    while True:
        try:
            num_players = int(input("Enter number of players: "))
            if num_players < 1:
                print("Enter at least 1 player.")
                continue
            break
        except ValueError:
            print("Invalid input. Enter a number.")

    score_data = []
    for i in range(1, num_players + 1):
        name = input(f"\nEnter name for Player-{i}: ").strip()
        while not name:
            print("Name cannot be empty!")
            name = input(f"Enter name for Player-{i}: ").strip()
        score, attempted = play_quiz(name)
        score_data.append((name, score, attempted))

    print("\nScore Summary:")
    for name, score, _ in score_data:
        print(f"{name}: {score}/4 correct")

    input("\nPress Enter to show score chart...")
    visualize_scores(score_data)

if __name__ == '__main__':
    main()
