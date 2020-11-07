# Takes in input string, prompt string, dictionary of factors.
# Keys in dictionary are our factors, values are tuples.
# First value of the tuple is 1 or 0, implying on or off.
# Second value is the weight of the specific factor.
# Returns calculated score.

from .factor import Factor


def main(n: str, prompt: str, factors: {str: (int, float)}) -> float:
    score = 0.0
    for f in factors:
        if factors[f][0] == 1:
            factor = Factor()
            score += factor.score(n, prompt) * factors[f][1]

# TODO: Modify factor variable according to factor
