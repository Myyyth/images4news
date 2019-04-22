import re

import gensim
from nltk import SnowballStemmer, WordNetLemmatizer
stemmer = SnowballStemmer('english')

def lemmatize_stemming(text):
    return stemmer.stem(WordNetLemmatizer().lemmatize(text, pos='v'))

# Tokenize and lemmatize
def preprocess(text):
    result = []
    for token in gensim.utils.simple_preprocess(text):
        if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
            result.append(lemmatize_stemming(token))
    return result

def get_keywords(text):
    pp_text = preprocess(text)
    dictionary = gensim.corpora.Dictionary([pp_text])
    #dictionary.filter_extremes(no_below=15, no_above=0.1)
    # convert document into bag of words
    bow_corpus = [dictionary.doc2bow(pp_text)]
    lda_model = gensim.models.LdaMulticore(bow_corpus,
                                           num_topics=3,
                                           id2word=dictionary,
                                           passes=1,
                                           workers=2)
    result = []
    for idx, topic in lda_model.print_topics(-1):
        topic_words = re.findall(r'"(.*?)"', topic)
        count = min(4, len(topic_words))
        query = []
        for i in range(count):
            if topic_words[i] not in query:
                query.append(topic_words[i])
        result.append(' '.join(query))
    return result