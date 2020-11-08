from .factor import Factor
import nltk


class Plagiarism(Factor):

    def _jaccard_similarity(self, source_text: [str], text: [str]) -> float:
        intersection = set(source_text).intersection(set(text))
        union = set(source_text).union(set(text))
        return len(intersection) / len(union)

    def score(self, text: str, args: list) -> float:
        source_text = args[0]
        #checks if this is a rephrasing example
        process_parity = args[1]
        max_limit = args[2]
        if not process_parity:
            return 0.0
        source_lst = nltk.word_tokenize(source_text)
        text_lst = nltk.word_tokenize(text)
        source_words = []
        text_words = []
        stop_words = nltk.corpus.stopwords.words("english")
        for word in source_lst:
            if word.lower() not in stop_words:
                source_words.append(word.lower())
        for word in text_lst:
            if word.lower() not in stop_words:
                text_words.append(word.lower())
        jaccard_score = self._jaccard_similarity(source_words, text_words)
        if jaccard_score < max_limit:
            return 1.0
        else:
            return 0.0
