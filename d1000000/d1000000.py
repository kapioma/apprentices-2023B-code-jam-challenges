"""
Name: d1000000.py
Last update: 18/04/2023
"""

from collections import defaultdict

def get_used_dice(dice_bucket : dict, max_die_value : int) -> int:
    used_dice = 0
    target_die = 1
    current_die = 1

    # Greedy algorithm, which takes all the possible dice to form a straight.
    while (current_die <= max_die_value):
        if (current_die >= target_die and dice_bucket[current_die] > 0):
            while (current_die >= target_die and dice_bucket[current_die] > 0):
                used_dice += 1
                dice_bucket[current_die] -= 1
                target_die += 1
        
        current_die += 1

    return used_dice
        

        

if __name__ == '__main__':
    testCases = int(input())

    for testCase in range(testCases):
        dice = int(input())
        # Keep track of the times a n sides die appears.
        dice_bucket = defaultdict(int)
        input_dice = map(int, input().split())
        # Keep the die with the max sides
        max_die_value = 0

        # Counting the dice and getting the die with the max sides.
        for die in input_dice:
            max_die_value = max(max_die_value, die)
            dice_bucket[die] += 1

        used_dice = get_used_dice(dice_bucket, max_die_value)
        print(f'Case #{testCase + 1}: {used_dice}')
        