import random
import time
from termcolor import cprint, colored

QUESTION = 'question'
OPTIONS = 'options'
ANSWER = 'answer'

class Quiz:
    def __init__(self, quiz_data, time_limit=15):
        self.quiz_data = quiz_data
        self.score = 0
        self.time_limit = time_limit

    def ask_question(self, index, question, options):
        cprint(f"\nQuestion {index}: {question}", 'cyan', attrs=['bold'])
        random.shuffle(options)  # shuffle answer options
        for opt in options:
            print(opt)

        start_time = time.time()
        user_answer = input(colored("Your answer: ", 'yellow')).upper().strip()
        elapsed_time = time.time() - start_time

        if elapsed_time > self.time_limit:
            cprint(f"⏰ Time's up! You took {elapsed_time:.1f}s.", 'red')
            return None

        return user_answer

    def run(self):
        random.shuffle(self.quiz_data)

        for index, item in enumerate(self.quiz_data, 1):
            answer = self.ask_question(index, item[QUESTION], item[OPTIONS][:])

            if not answer:
                cprint(f"Correct answer: {item[ANSWER]}", 'red')
                continue

            if answer in item[ANSWER]:  # supports multiple answers
                cprint('✅ Correct!', 'green', attrs=['bold'])
                self.score += 1
            else:
                cprint(f"❌ Wrong! Correct answer: {item[ANSWER]}", 'red')

        self.show_results()

    def show_results(self):
        total = len(self.quiz_data)
        percentage = (self.score / total) * 100

        cprint("\n===== QUIZ OVER =====", 'magenta', attrs=['bold'])
        cprint(f"Your final score: {self.score}/{total} ({percentage:.1f}%)", 'cyan')

        if percentage == 100:
            cprint("🎉 Excellent! Perfect score!", 'green', attrs=['bold'])
        elif percentage >= 70:
            cprint("👏 Great job!", 'green')
        elif percentage >= 40:
            cprint("🙂 Not bad, keep practicing!", 'yellow')
        else:
            cprint("😢 Better luck next time!", 'red')


def main():
    quiz_questions = [
        {QUESTION: 'What is the capital of France?', OPTIONS: ['A. Berlin', 'B. Madrid', 'C. Paris', 'D. Rome'], ANSWER: ['C']},
        {QUESTION: 'Which planet is known as the Red Planet?', OPTIONS: ['A. Earth', 'B. Mars', 'C. Jupiter', 'D. Saturn'], ANSWER: ['B']},
        {QUESTION: 'What is the largest ocean on Earth?', OPTIONS: ['A. Atlantic', 'B. Indian', 'C. Arctic', 'D. Pacific'], ANSWER: ['D']},
        {QUESTION: 'Which of the following are programming languages?', OPTIONS: ['A. Python', 'B. HTML', 'C. Java', 'D. CSS'], ANSWER: ['A','C']},
        {QUESTION: 'Who developed the theory of relativity?', OPTIONS: ['A. Isaac Newton', 'B. Albert Einstein', 'C. Galileo Galilei', 'D. Nikola Tesla'], ANSWER: ['B']},
        {QUESTION: 'What is the hardest natural substance?', OPTIONS: ['A. Diamond', 'B. Gold', 'C. Iron', 'D. Quartz'], ANSWER: ['A']},
        {QUESTION: 'Which gas do plants absorb during photosynthesis?', OPTIONS: ['A. Oxygen', 'B. Nitrogen', 'C. Carbon Dioxide', 'D. Hydrogen'], ANSWER: ['C']},
        {QUESTION: 'What is the smallest prime number?', OPTIONS: ['A. 0', 'B. 1', 'C. 2', 'D. 3'], ANSWER: ['C']},
        {QUESTION: 'Which country is known as the Land of the Rising Sun?', OPTIONS: ['A. China', 'B. Japan', 'C. Thailand', 'D. India'], ANSWER: ['B']},
        {QUESTION: 'What is the boiling point of water at sea level?', OPTIONS: ['A. 90°C', 'B. 100°C', 'C. 110°C', 'D. 120°C'], ANSWER: ['B']},
        {QUESTION: 'Which continent is the Sahara Desert located in?', OPTIONS: ['A. Asia', 'B. Africa', 'C. Australia', 'D. North America'], ANSWER: ['B']},
        {QUESTION: 'What is the chemical symbol for Gold?', OPTIONS: ['A. Au', 'B. Ag', 'C. Gd', 'D. Go'], ANSWER: ['A']},
        {QUESTION: 'Who is the author of "Harry Potter" series?', OPTIONS: ['A. J.R.R. Tolkien', 'B. J.K. Rowling', 'C. George R.R. Martin', 'D. Suzanne Collins'], ANSWER: ['B']},
        {QUESTION: 'What is the largest mammal on Earth?', OPTIONS: ['A. Elephant', 'B. Blue Whale', 'C. Giraffe', 'D. Orca'], ANSWER: ['B']},
        {QUESTION: 'Which instrument is used to measure temperature?', OPTIONS: ['A. Barometer', 'B. Thermometer', 'C. Hygrometer', 'D. Altimeter'], ANSWER: ['B']},
        {QUESTION: 'Which is the fastest land animal?', OPTIONS: ['A. Cheetah', 'B. Lion', 'C. Horse', 'D. Tiger'], ANSWER: ['A']},
        {QUESTION: 'In which year did World War II end?', OPTIONS: ['A. 1942', 'B. 1945', 'C. 1948', 'D. 1950'], ANSWER: ['B']},
        {QUESTION: 'What is the main gas found in the air we breathe?', OPTIONS: ['A. Oxygen', 'B. Carbon Dioxide', 'C. Nitrogen', 'D. Hydrogen'], ANSWER: ['C']},
        {QUESTION: 'Which planet has the most moons?', OPTIONS: ['A. Earth', 'B. Jupiter', 'C. Mars', 'D. Saturn'], ANSWER: ['D']},
        {QUESTION: 'What is the square root of 144?', OPTIONS: ['A. 10', 'B. 11', 'C. 12', 'D. 13'], ANSWER: ['C']}
    ]

    quiz = Quiz(quiz_questions, time_limit=20)
    quiz.run()


if __name__ == '__main__':
    main()
