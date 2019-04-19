from googleapiclient.discovery import build
from image_search import search_store, download_image
from rake import get_keywords

news = open('news.txt', 'r').read()
keywords = get_keywords(news)
query = ''
for i in range(5):
    query += '{0} '.format(keywords[i])
search_store(2, 5, query)
