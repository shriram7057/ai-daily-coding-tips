"""
Scheduler Logic
----------------
Controls when tips are generated.

Goals:
- Avoid spammy automation
- Simulate healthy maintenance activity
- Limit daily posts
"""

import random
from datetime import datetime

# Allowed hours (24-hour format)
ACTIVE_HOURS = [9, 11, 13, 15, 18, 21]

# Probability of generation per hour
GENERATION_CHANCE = 0.65


def should_generate():
    """
    Decide whether content should be generated.
    """

    now = datetime.now()
    current_hour = now.hour

    if current_hour not in ACTIVE_HOURS:
        print("Outside active hours.")
        return False

    decision = random.random() < GENERATION_CHANCE

    if decision:
        print("Scheduler approved generation.")
    else:
        print("Scheduler skipped generation.")

    return decision


if __name__ == "__main__":
    approved = should_generate()

    if approved:
        exit(0)

    exit(1)