from rake_nltk import Rake, Metric


def get_keywords(text):
    r = Rake(ranking_metric=Metric.WORD_FREQUENCY)
    r.extract_keywords_from_text(text)
    return r.get_ranked_phrases()
