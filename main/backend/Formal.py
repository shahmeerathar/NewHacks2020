from .factor import Factor
import nltk


class Formal(Factor):
    def score(self, n: str, prompt: str) -> float:
        return 1.0