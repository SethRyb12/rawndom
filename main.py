#!/usr/bin/env python3
import random

MESSAGES = [
    "Keep going — small steps win races.",
    "Creativity demands a little chaos.",
    "Ship early. Ship often.",
    "Refactor mercilessly.",
    "Take a break; return stronger.",
    "Experiment daily; learn quickly.",
    "Solve one problem today, another tomorrow.",
    "Read code; read people; read the world.",
    "Make tiny bets and measure outcomes.",
    "Comments are for humans; tests are for machines.",
    "Ask good questions; your future self will thank you.",
    "Keep a changelog — future you will love it.",
    "Automate repetitive work; free time fuels creativity.",
    "Design for clarity, not cleverness.",
    "Pair program: two minds shorten feedback loops.",
    "Progress is messy; ship the best you have.",
    "Celebrate small wins; they compound into momentum.",
    "Name things clearly; names are documentation.",
    "Write code you can explain in one sentence.",
    "Learn by building, then by breaking and fixing.",
    "Fix the cause, not just the symptom.",
    "A bug found today is a lesson for tomorrow.",
    "Keep your functions short and your variables descriptive.",
    "Don't optimize what you haven't measured.",
    "If you can't explain it simply, you don't understand it yet.",
    "Hardcoded values are debts you'll pay back with interest.",
    "The best code is the code you didn't have to write.",
    "Done is better than perfect.",
]

def main():
    print(random.choice(MESSAGES))

if __name__ == '__main__':
    main()
