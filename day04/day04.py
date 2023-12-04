fn = "data.txt"

lines = open(fn).read().split("\n")

# Part 1
all_scores = []
for line in lines:
    score = 0
    numbers = line.split(":")[1]
    winning_numbers = [int(n) for n in numbers.split("|")[0].strip().split()]
    elf_numbers = [int(n) for n in numbers.split("|")[1].strip().split()]
    # Card matches
    matches = set(elf_numbers).intersection(set(winning_numbers))
    # Lets give the score
    if len(matches) > 1:
        score = 2 ** (len(matches) - 1)
    elif len(matches) == 1:
        score = 1

    all_scores.append(score)
print(sum(all_scores))

# Part 2 : Copy same code to keep the original
card_tracker = {}  # Tracks the card and matches
card_number_tracker = {}  # Tracks how many cards of each

for line in lines:
    score = 0
    numbers = line.split(":")[1]
    card_id = int(line.split(":")[0].split()[1])
    card_number_tracker.update({card_id: 1})
    winning_numbers = [int(n) for n in numbers.split("|")[0].strip().split()]
    elf_numbers = [int(n) for n in numbers.split("|")[1].strip().split()]

    # Card matches
    matches = set(elf_numbers).intersection(set(winning_numbers))
    card_tracker.update({card_id: len(matches)})  # Matches per card

# Let the scratchard rain begin
for card, matches in card_tracker.items():
    multiplier = card_number_tracker[card]
    for m in range(1, matches + 1):
        next_card_id = card + m
        num_cards = card_number_tracker[next_card_id] + 1 * multiplier
        card_number_tracker.update({next_card_id: num_cards})

print(sum([i for i in card_number_tracker.values()]))
