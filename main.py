#!/usr/bin/env python3
import random

MESSAGES = [
    "Keep going — small steps win races.",
    "Creativity demands a little chaos.",
    "Ship early. Ship often.",
    "Refactor mercilessly.",
    "Take a break; return stronger.",
    "Experiment daily; learn quickly.",
]

def main():
    print(random.choice(MESSAGES))

if __name__ == '__main__':
    main()
