from googleapiclient.discovery import build
import requests
import os
import json

api = 'AIzaSyC93OUGHwRdKGFRTj29DLHitMyjiXg-7GI'
cx = '013647856763265462959:2bv6b82j20i'


custom_search = build("customsearch", "v1",
                       developerKey=api)


def search_store(news_id, k, q):
    if not os.path.isdir(str(news_id)):
        os.mkdir(str(news_id))
    res = custom_search.cse().list(
              q=q,
              cx=cx,
              searchType='image'
        ).execute()
    for i, item in enumerate(res['items']):
        if i >= k:
            break
        download_image(item['link'], str(news_id))


def download_image(url, folder):
    filename = url.split('/')[-1]
    if '?' in filename:
        filename = filename.split('?')[0]
    r = requests.get(url, allow_redirects=True)
    open('{0}/{1}'.format(folder, filename), 'wb').write(r.content)

