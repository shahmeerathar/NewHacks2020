import os

from .factor import Factor
from google.cloud import language_v1

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/shahmeerathar/Documents/Computer Science/Hackathons/NewHacks/Project/main/backend/NewHacks-9a3ddc3e13de.json'
client = language_v1.LanguageServiceClient()


class Sentiment(Factor):
    def score(self, n: str, args: list) -> float:
        # sentiment = args[0]  # Only one argument, neutral or passionate
        document = language_v1.Document(content=n,
                                        type_=language_v1.Document.Type.PLAIN_TEXT)
        annotations = client.analyze_sentiment(request={'document': document})
        magnitude = annotations.document_sentiment.magnitude
        if args[0] == 'neutral':
            return 1 - (magnitude - 0.0)
        else:
            return 1 - (1.0 - magnitude)
