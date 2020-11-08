from .factor import Factor
import nltk
import rake_nltk


class FKGL(Factor):
    def score(self, text: str, args: list) -> float:
        source_text = args[0]
        #checks if this is a rephrasing example
        process_parity = args[1]
        if not process_parity:
            return 0.0
        r = rake_nltk.Rake(max_length= 3)
        r.extract_keywords_from_text(source_text)
        # getting top 10 key words/phrases
        keyword_max = round(0.05*len(nltk.word_tokenize(source_text)))
        phrases_original = r.get_ranked_phrases()[:keyword_max]
        r.extract_keywords_from_text(text)
        phrases_text = r.get_ranked_phrases()[:round(0.10*len(nltk.word_tokenize(text)))]
        #count how many of the ranked phrases appear as keywords in the user's text
        phrase_count = 0
        for phrase in phrases_original:
            if phrase in phrases_text:
                phrase_count += 1
        return phrase_count/keyword_max



