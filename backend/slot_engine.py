# slot_engine.py

import random

from slot_config import NUM_REELS, NUM_ROWS, SYMBOL_IDS, PAYLINES, PAYOUTS

def spin_once():
    return [
        [random.choice(SYMBOL_IDS) for i in range(NUM_ROWS)]
        for i in range(NUM_REELS)
    ]

def to_rows(grid):
    """
    Convert reel-major grid (5x3) to row-major (3x5).
    """
    rows = []
    for row in range(NUM_ROWS):
        rows.append([grid[reel][row] for reel in range(NUM_REELS)])
    return rows

from slot_config import PAYLINES  # add this to your imports at the top

def symbols_on_payline(grid, payline):
    """
    return the list of symbol_ids along that line.
    """
    symbols = []
    for reel_index, row_index in payline:
        symbols.append(grid[reel_index][row_index])
    return symbols

def evaluate_line(symbols_on_line):
    """
    Given a list of symbols from a single payline, return the payout
    for that line according to the PAYOUTS table.

    - We count how many matching symbols we have from the left.
    - Then we look up (symbol, count) in the PAYOUTS dict.
    """
    if not symbols_on_line:
        return 0

    first_symbol = symbols_on_line[0]

    # Count how many symbols from the left match the first one
    count = 1
    for symbol in symbols_on_line[1:]:
        if symbol == first_symbol:
            count += 1
        else:
            break

    # Get the payout table for this symbol (or empty dict if not found)
    symbol_payouts = PAYOUTS.get(first_symbol, {})

    # Return the payout for this count, or 0 if there's no entry
    return symbol_payouts.get(count, 0)

def evaluate_spin(grid):
    """
    Evaluate all paylines
    """
    total_win = 0

    for payline in PAYLINES:
        line_symbols = symbols_on_payline(grid, payline)
        line_win = evaluate_line(line_symbols)
        total_win += line_win

    return total_win

if __name__ == "__main__":
    result = spin_once()

    print("Grid (reel-major):")
    for reel in result:
        print(reel)

    print("\nPaylines:")
    for i, payline in enumerate(PAYLINES, start=1):
        line_symbols = symbols_on_payline(result, payline)
        line_win = evaluate_line(line_symbols)
        print(f"Line {i}: {line_symbols} -> win: {line_win}")

    total = evaluate_spin(result)
    print(f"\nTotal win for this spin: {total}")

# result = spin_once()
# print("Grid (reel-major):")
# for reel in result:
#     print(reel)
#
# print("\nPaylines:")
# for i, payline in enumerate(PAYLINES, start=1):
#     line_symbols = symbols_on_payline(result, payline)
#     print(f"Line {i}: {line_symbols}")
