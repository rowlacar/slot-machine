# slot_config.py

# Core layout
NUM_REELS = 5
NUM_ROWS = 3

# symbol identifiers
SYMBOL_IDS = [
    "HIGH_A",
    "MID_A",
    "LOW_A",
]

# [(reel index, row index)]
# a list [of lists[of tuples (column, row)]]
PAYLINES = [
    # Line 1: Top row
    [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)],

    # Line 2: Middle row
    [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1)],

    # Line 3: Bottom row
    [(0, 2), (1, 2), (2, 2), (3, 2), (4, 2)],

    # Line 4: Diagonal from top-left to bottom-right
    [(0, 0), (1, 1), (2, 2), (3, 1), (4, 0)],

    # Line 5: Diagonal from bottom-left to top-right
    [(0, 2), (1, 1), (2, 0), (3, 1), (4, 2)],
]

PAYOUTS = {
    "HIGH_A": { 3: 0, 4: 20, 5: 50 },
    "MID_A":  { 3: 0, 4: 1, 5: 20 },
    "LOW_A":  { 3: 0, 4: 0,  5: 10 },
}
