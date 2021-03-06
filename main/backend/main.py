# Takes in input string, prompt string, dictionary of factors.
# Keys in dictionary are our factors, values are tuples.
# First value of the tuple is 1 or 0, implying on or off.
# Second value is the weight of the specific factor.
# Third value is the factor val itself.
# Returns calculated score.

from .FKGL import FKGL
from .sentiment import Sentiment
from .keyword import Keyword
from .plagiarism import Plagiarism


def get_score(n: str, source: str, factors: {str: (int, float, str)}) -> float:
    score = 0.0
    for f in factors:
        if factors[f][0] == 1:
            if f == 'FKGL':
                factor = FKGL()
                arguments = [factors[f][2]]
            if f == 'sentiment':
                factor = Sentiment()
                arguments = [factors[f][2]]
            if f == 'keyword':
                factor = Keyword()
                arguments = [source, factors[f][2]]
            if f == 'plagiarism':
                factor = Plagiarism()
                arguments = [source, factors[f][2]]
            score += factor.score(n, arguments) * factors[f][1]
    return score
