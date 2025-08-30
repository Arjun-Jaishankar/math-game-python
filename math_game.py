import random

def main():
    score = 0
    for count in range(1, 16):
        if count <= 5:
            a, b = random.randint(1, 10), random.randint(1, 10)
            op = random.choice(['+', '-', '*', '/'])
            question = f"Q{count}: {a} {op} {b} = ?"
            answer = eval(f"{a}{op}{b}")
        elif count <= 10:
            a, b, c = random.randint(1,10), random.randint(1,10), random.randint(1,10)
            op1, op2 = random.choice(['+', '-', '*', '/']), random.choice(['+', '-', '*', '/'])
            question = f"Q{count}: {a} {op1} {b} {op2} {c} = ?"
            answer = eval(f"{a}{op1}{b}{op2}{c}")
        else:
            a, b, c, d = random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10)
            op1, op2, op3 = random.choice(['+', '-', '*', '/']), random.choice(['+', '-', '*', '/']), random.choice(['+', '-', '*', '/'])
            question = f"Q{count}: {a} {op1} {b} {op2} {c} {op3} {d} = ?"
            answer = eval(f"{a}{op1}{b}{op2}{c}{op3}{d}")

        print(question)
        try:
            user = float(input("Your answer: "))
            if abs(user - answer) < 1e-2:
                score += 10
                print("Correct! Score:", score)
            else:
                print(f"Incorrect! Final score: {score}")
                break
        except Exception as e:
            print("Invalid input.", e)
            break
    print(f"Game Over. Final Score: {score}")

if __name__ == '__main__':
    main()
