import random
import time

def generate_question():
    """Generate a random math question."""
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*'])
    
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2

    return f"{num1} {operator} {num2}", answer

def math_challenge(num_questions, time_limit):
    """Run the math challenge."""
    score = 0
    start_time = time.time()
    
    for _ in range(num_questions):
        question, correct_answer = generate_question()
        print(f"Solve: {question}")
        
        try:
            user_answer = input(f"Your answer (you have {time_limit} seconds): ")
            elapsed_time = time.time() - start_time
            
            if elapsed_time > time_limit:
                print("Time's up!")
                break
            
            if int(user_answer) == correct_answer:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer was {correct_answer}.")
        except ValueError:
            print("Invalid input! Please enter a number.")
        
        print(f"Elapsed time: {elapsed_time:.2f} seconds\n")

    print(f"Your final score: {score}/{num_questions}")

def main():
    """Main function to run the challenge."""
    print("Welcome to the Timed Math Challenge!")
    num_questions = int(input("How many questions would you like to answer? "))
    time_limit = int(input("What is the time limit for each question (in seconds)? "))
    
    math_challenge(num_questions, time_limit)

if __name__ == "__main__":
    main()
