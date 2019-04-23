import requests
from images4news.lda import get_keywords as get_keywords_lda
from images4news.image_search import search
url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=531ee81609404252900df1e72daa470c')
response = requests.get(url).json()
i = 1
with open('news_examples/output.txt', 'w') as f:
    for article in response['articles']:
        content = ''
        if article['title'] is not None:
            content += article['title']
        if article['description'] is not None:
            content += ' ' + article['description']
        if article['content'] is not None:
            content += ' ' + article['content']
        keywords = get_keywords_lda(content)
        total = []
        for keyword in keywords:
            total.extend(keyword.split())
        total = list(set(total))
        f.write(str(i) + '. ' + str(total) + '\n' + str(search(3, ' '.join(total))) + '\n')
        f.write('\n')
        i += 1
        if i == 10:
            break