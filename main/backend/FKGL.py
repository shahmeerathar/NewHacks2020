import nltk
import syllables
from .factor import Factor


class FKGL(Factor):
    def score(self, text: str, args: list) -> float:
        # defining appropriate FKGL score for each audience level
        # Only one argument in args, which is audience.
        audience = args[0]
        desired_scores = {"basic": 70.0, "intermediate": 55.0,
                          "difficult": 40.0}
        """the FKGL score is computed using the following equation: 
        206.835-1.015(total words/total sentences)-84.6(total syllables/total 
        words) """
        total_sentences = len(nltk.sent_tokenize(text))
        words = nltk.word_tokenize(text)
        total_words = len(words)
        total_syllables = 0
        for word in words:
            total_syllables += syllables.estimate(word)
        fkgl_score = 206.835 - 1.015 * (
                    total_words / total_sentences) - 84.6 * (
                                 total_syllables / total_words)
        # Calculating how many multiples of 5 it is away from the desired FKGL
        deviation = (abs(fkgl_score - desired_scores[audience])) / 5
        to_subtract = deviation * 0.2
        if to_subtract > 1:
            grade = 0
        else:
            grade = 1 - to_subtract
        return grade
