import operator
from collections import Counter

fn = "data.txt"
lines = open(fn).read().split("\n")


def make_numbers(card):
    "Converts the letter cards to numbers"
    # Convert letters to numbers
    mapping = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "J": 1,  # Part 1 : 11
        "T": 10,
        "9": 9,
        "8": 8,
        "7": 7,
        "6": 6,
        "5": 5,
        "4": 4,
        "3": 3,
        "2": 2,
    }
    return [mapping[a] for a in card]


def check_joker(c):
    if "J" in c.keys():
        return c["J"]
    else:
        return 0


def group_card(card):
    "Groups the card to the hand type"

    # Use the info from the counter and group the card
    c = Counter(card)

    # Five of a Kind
    if 5 in c.values():
        return 0
    # Four of a kind
    elif 4 in c.values():
        if check_joker(c) > 0:
            modifier = 1
        else:
            modifier = 0
        return 1 - modifier
    # Full House
    elif (3 in c.values()) & (2 in c.values()):
        if check_joker(c) > 0:
            modifier = 2
        else:
            modifier = 0
        return 2 - modifier
    # Three of a kind
    elif (3 in c.values()) & (sum([a == 1 for a in c.values()]) == 2):
        if check_joker(c) == 3:
            modifier = 2
        elif check_joker(c) == 1:
            modifier = 2
        elif check_joker(c) == 0:
            modifier = 0
        else:
            print("Something fishy")
        return 3 - modifier

    # Two pair
    elif (2 in c.values()) & (sum([a == 2 for a in c.values()]) == 2):
        if check_joker(c) == 2:
            modifier = 3
        elif check_joker(c) == 1:
            modifier = 2
        else:
            modifier = 0

        return 4 - modifier
    # One pair
    elif (2 in c.values()) & (sum([a == 2 for a in c.values()]) == 1):
        if check_joker(c) > 0:
            modifier = 2  # Can get three of a kind
        else:
            modifier = 0
        return 5 - modifier  #
    # High card
    elif sum([a == 1 for a in c.values()]) == 5:
        if check_joker(c) > 0:
            modifier = 1
        else:
            modifier = 0
        return 6 - modifier  # Check joker tiene que ser 1

    else:
        print("Something is wrong")
        return -1


def sort_tuples(group):
    # Sort the tuples by the different keys in each group
    # Sort by the card numbers, not by the rank
    return sorted(group, key=operator.itemgetter(0, 1, 2, 3, 4), reverse=False)


groups = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
# Parsing of input
for line in lines:
    card = [a for a in line.split(" ")[0]]
    g = group_card(card)
    card = make_numbers(card)  # If part 1, shift this line before assigning to groups
    bet = int(line.split(" ")[1])
    # Add card to group, with the bet at the end
    groups[g].append(tuple(card + [bet]))

g_order = list(range(0, 7))
g_order.reverse()
tw = 0
rank = 0
for i in g_order:
    gd = groups[i]
    r_sorted_group = sort_tuples(gd)
    for wc in r_sorted_group:
        rank += 1
        tw += rank * wc[-1]
print(tw)
