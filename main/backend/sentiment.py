from .factor import Factor
import nltk


class Sentiment(Factor):
    def score(self, n: str, prompt: str) -> float:
        return 1.0
