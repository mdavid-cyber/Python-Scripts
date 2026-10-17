import random

# start the throw counter
throws = 0

# roll two dice for the first time
die1 = random.randint(1, 6)
die2 = random.randint(1, 6)

# keep rolling until they match
while die1 != die2:
    throws += 1  # count this throw
    print(f"Roll {throws}: {die1} and {die2} — not a match, rolling again...")
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)

# when dice match, exit loop
throws += 1  # count the final matching roll too
print(f"🎉 Matched! You rolled {die1} and {die2} after {throws} throws.")
