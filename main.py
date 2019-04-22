from images4news.image_search import search
from images4news.rake import get_keywords as get_keywords_rake
from images4news.lda import get_keywords as get_keywords_lda
from images4news.pachinko import get_keywords as get_keywords_pachinko
news = open('news_examples/news1.txt', 'r').read()
keywords = get_keywords_lda(news)
#keywords = get_keywords_pachinko('../news_examples/')
print(keywords)
# query = ''
# for i in range(5):
#     query += '{0} '.format(keywords[i])
# search(5, query)
