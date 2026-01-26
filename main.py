#!/usr/bin/env python3
import argparse
import json
import random
import sys

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
    "Release often; feedback is the only real compass.",
    "Your code is a conversation with the next person who reads it.",
    "Strive for simplicity; complexity is easy, clarity is hard.",
    "Version control is your time machine; use it often.",
    "Sleep on it; the subconscious is a great debugger.",
    "Every 'error' is just data in disguise.",
    "Stay curious; the tech moves fast, but fundamentals are forever.",
    "Documentation is a love letter to your future self.",
    "Break the problem down until the pieces are boring.",
    "The most expensive part of a project is the part you built too soon.",
]


def get_messages(count=1, seed=None):
    if seed is not None:
        random.seed(seed)
    return [random.choice(MESSAGES) for _ in range(count)]


def build_parser():
    p = argparse.ArgumentParser(
        prog="rawndom",
        description="Print one or more random inspirational messages",
    )
    p.add_argument("-n", "--count", type=int, default=1, help="number of messages to print")
    p.add_argument("-s", "--seed", type=int, default=None, help="optional RNG seed for reproducible output")
    p.add_argument("--json", action="store_true", help="output messages as a JSON array")
    p.add_argument("--list", action="store_true", help="print all available messages and exit")
    return p


def main(argv=None):
    argv = argv if argv is not None else sys.argv[1:]
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.list:
        for m in MESSAGES:
            print(m)
        return 0

    msgs = get_messages(count=max(1, args.count), seed=args.seed)

    if args.json:
        json.dump(msgs, sys.stdout, ensure_ascii=False)
        sys.stdout.write("\n")
    else:
        for m in msgs:
            print(m)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
