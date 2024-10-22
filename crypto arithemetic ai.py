import itertools

# Function to solve the cryptarithmetic problem SEND + MORE = MONEY
def solve_cryptarithmetic():
    # Unique letters in the equation
    letters = 'SENDMORY'

    # Generate all possible digit assignments for the letters
    for digits in itertools.permutations(range(10), len(letters)):
        # Create a dictionary mapping each letter to a digit
        mapping = dict(zip(letters, digits))

        # Ensure no leading zeroes in the numbers (S and M cannot be 0)
        if mapping['S'] == 0 or mapping['M'] == 0:
            continue

        # Calculate the values of SEND, MORE, and MONEY based on the current mapping
        send = 1000 * mapping['S'] + 100 * mapping['E'] + 10 * mapping['N'] + mapping['D']
        more = 1000 * mapping['M'] + 100 * mapping['O'] + 10 * mapping['R'] + mapping['E']
        money = 10000 * mapping['M'] + 1000 * mapping['O'] + 100 * mapping['N'] + 10 * mapping['E'] + mapping['Y']

        # Check if SEND + MORE equals MONEY
        if send + more == money:
            print(f"SEND + MORE = MONEY")
            print(f"{send} + {more} = {money}")
            print(f"Mapping: {mapping}")
            return

    print("No solution found.")

# Solve the cryptarithmetic puzzle
solve_cryptarithmetic()
