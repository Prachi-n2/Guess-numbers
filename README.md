A concise README.md for the number/random scripts.
# Random Number & Guessing Games

Simple collection of Python examples demonstrating the `random` module and small CLI games (number guessing, computer-guess demo, card shuffle, etc.).

## Files
- Main script: `random%20number.py`  
  Recommended: rename to `random_number.py` (remove spaces/percent encoding).

## Requirements
- Python 3.8+

# Run
From the project folder (PowerShell):
.\.venv\Scripts\Activate
python `random%20number.py`
Or after renaming:
python `random_number.py`

# Usage
The script runs a number guessing game. Enter integer guesses when prompted.
Prompts and ranges are displayed (default: 1 to 10).
Press Ctrl+C to exit early.

# Quick fixes & suggestions
Rename random%20number.py to random_number.py to avoid shell/IDE issues.
Remove duplicate import random lines.
Validate input: wrap int(input(...)) in try/except and reject out-of-range values.
Handle KeyboardInterrupt to exit cleanly.
Consider extracting game logic into functions and using if __name__ == "__main__": for easier testing.
For deterministic behavior in tests, accept a --seed CLI argument and call random.seed().

# Troubleshooting
ValueError on input: provide integers or update the script to validate input.
No output: ensure the correct Python interpreter is used and the terminal is focused.
If time/performance issues occur, check for blocking calls in other commented examples.

## Install (Windows / PowerShell)
```powershell
python -m venv .venv
.\.venv\Scripts\Activate
pip install --upgrade pip
