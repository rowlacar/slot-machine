from slot_engine import spin_once, evaluate_spin


def run_simulation(num_spins: int):
    """
    Run a simulation of num_spins spins

    Returns a dict with summary statistics:
        - total_multiplier
        - average_multiplier
        - max_multiplier
        - num_spins
    """

    total_multiplier = 0
    max_multiplier = 0

    for _ in range(num_spins):
        grid = spin_once()
        multiplier = evaluate_spin(grid)
        total_multiplier += multiplier
        if multiplier > max_multiplier:
            max_multiplier = multiplier

    avg_multiplier = total_multiplier / num_spins if num_spins > 0 else 0

    return {
        "num_spins": num_spins,
        "total_multiplier": total_multiplier,
        "average_multiplier": avg_multiplier,
        "max_multiplier": max_multiplier,
    }
