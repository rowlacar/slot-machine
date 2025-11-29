# slot_engine.py

import random

from slot_config import NUM_REELS, NUM_ROWS, SYMBOL_IDS, PAYLINES, PAYOUTS

class GameSession:
    def __init__(self, starting_balance: int, bet_per_spin: int):
        """
        Represents a slot session.

        :param starting_balance: how many credits the player starts with
        :param bet_per_spin: how many credits are bet on each spin
        """
        self.balance = starting_balance
        self.bet_per_spin = bet_per_spin

    def set_bet(self, new_bet: int):
        """
        Change the bet per spin. Must be a positive integer.
        """
        if new_bet <= 0:
            raise ValueError("Bet per spin must be positive.")
        self.bet_per_spin = new_bet

    def can_afford_spin(self) -> bool:
        return self.balance >= self.bet_per_spin

    def place_bet(self):
        if not self.can_afford_spin():
            raise ValueError("Insufficient balance for spin.")
        self.balance -= self.bet_per_spin

    def spin(self):
        if not self.can_afford_spin():
            raise ValueError("Insufficient balance for spin.")

        self.place_bet()                                        # Deduct
        grid = spin_once()                                      # Spin
        total_multiplier = evaluate_spin(grid)                  # sum of multipliers
        win_amount = total_multiplier * self.bet_per_spin       # convert to credits
        self.balance += win_amount                              # add to balance

        return {
            "grid_reel_major": grid,
            "grid_row_major": to_rows(grid),
            "multiplier": total_multiplier,
            "win": win_amount,  # actual credits won
            "balance": self.balance,  # updated balance after win
        }

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

    - Count how many matching symbols we have from the left.
    - Then look up (symbol, count) in PAYOUTS
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
    session = GameSession(10, 3)
    result = session.spin()
    print(result)
    print (session.balance)

# if __name__ == "__main__":
#     session = GameSession(10, 3)
#     grid, win = session.spin()
#     print("Grid:", grid)
#     print("Win:", win)
#     print("Balance after spin:", session.balance)

# if __name__ == "__main__":
#     session = GameSession(10, 3)
#     print("Starting balance:", session.balance)
#
#     session.place_bet()
#     print("After first bet:", session.balance)
#
#     session.place_bet()
#     print("After second bet:", session.balance)

# result = spin_once()
# print("Grid (reel-major):")
# for reel in result:
#     print(reel)
#
# print("\nPaylines:")
# for i, payline in enumerate(PAYLINES, start=1):
#     line_symbols = symbols_on_payline(result, payline)
#     print(f"Line {i}: {line_symbols}")
