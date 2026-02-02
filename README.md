# Yay — Random Project

A tiny Python CLI that prints a random inspirational message.

Quick start

```bash
python main.py            # print one random message
python main.py -n 3       # print three messages
python main.py -s 42      # deterministic output using seed
python main.py --list     # print all available messages
python main.py --from-file messages.txt  # load messages from a file
python main.py --json     # output as JSON array
```

Output to a file

```bash
python main.py -n 5 -o out.txt
python main.py --json -o out.json
```

Tests

```bash
# from the repository root
python -u "Yay-random-project/tests/test_main.py"
```

Files in this folder
- `main.py` — CLI script
- `tests/test_main.py` — unit tests
- `requirements.txt` — minimal dependencies (if any)
- `.gitignore`
