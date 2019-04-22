from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json
from .rake import get_keywords
from .image_search import search


@api_view(['GET', 'POST'])
def search_image(requst):
    if requst.method == 'GET':
        response = {
            'example': {
                'text': 'Tesla',
                'amount': 5
            }
        }
        return Response(response, status=status.HTTP_200_OK)
    elif requst.method == 'POST':
        response = {
            'error': False,
            'keyphrases': None,
            'links': None
        }
        if requst.body is not None:
            data = requst.data
            keyphrases = get_keywords(data['text'])
            query = ''
            phrases_amount = 1
            for i in range(phrases_amount):
                if i < len(keyphrases):
                    query += '{0} '.format(keyphrases[i])
            images = search(int(data['amount']), query)
            response['keyphrases'] = keyphrases[:5]
            response['links'] = images
            return Response(response, status=status.HTTP_200_OK)
        response['error'] = True
        return Response(response, status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_400_BAD_REQUEST)
