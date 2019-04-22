import RAKE


def get_keywords(text):
    r = RAKE.Rake(RAKE.GoogleSearchStopList())
    return r.run(text, 1, 4, 1)
