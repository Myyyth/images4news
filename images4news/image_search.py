from googleapiclient.discovery import build
import requests
import os

api = 'AIzaSyC93OUGHwRdKGFRTj29DLHitMyjiXg-7GI'
cx = '013647856763265462959:2bv6b82j20i'


custom_search = build("customsearch", "v1", developerKey=api)


def search(k, q):
    res = custom_search.cse().list(
              q=q,
              cx=cx,
              searchType='image'
        ).execute()
    return [item['link'] for i, item in enumerate(res['items']) if i <= k]


def download_images(urls, folder_name):
    for url in urls:
        filename = url.split('/')[-1]
        if '?' in filename:
            filename = filename.split('?')[0]
        r = requests.get(url, allow_redirects=True)
        if not os.path.isdir(folder_name):
            os.mkdir(folder_name)
        open('{0}/{1}'.format(folder_name, filename), 'wb').write(r.content)

