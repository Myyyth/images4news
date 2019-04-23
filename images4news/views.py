from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .rake import get_keywords as rake_get_keywords
from .lda import get_keywords as lda_get_keywords
from .pachinko import get_keywords as pachinko_get_keywords
from .image_search import search


@api_view(['GET', 'POST'])
def search_image(requst):
    if requst.method == 'GET':
        response = {
            'example': {
                'text': 'Tesla',
                'method': 'lda',
                'amount': 5
            }
        }
        return Response(response, status=status.HTTP_200_OK)
    elif requst.method == 'POST':
        response = {
            'error': False,
            'keywords': None,
            'method': None,
            'links': None
        }
        if requst.body is not None:
            data = requst.data
            if data['method'] == 'rake':
                keywords = rake_get_keywords(data['text'])
            elif data['method'] == 'lda':
                keywords = lda_get_keywords(data['text'])
            elif data['method'] == 'pachinko':
                open('temp_text.txt', 'w').write(data['text'])
                keywords = pachinko_get_keywords('temp_text.txt')
            else:
                response['error'] = True
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
            phrases_amount = 3
            total = []
            for i, keyword in enumerate(keywords):
                if i < phrases_amount:
                    total.extend(keyword.split())
            total = list(set(total))
            images = search(int(data['amount']), ' '.join(total))
            response['keywords'] = keywords[:5]
            response['links'] = images
            return Response(response, status=status.HTTP_200_OK)
        response['error'] = True
        return Response(response, status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_400_BAD_REQUEST)
