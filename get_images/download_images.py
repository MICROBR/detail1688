import sys
import os
import requests
from bs4 import BeautifulSoup
import urllib.request
import re
from PIL import Image
# import errno


class Downloader:
    def __init__(self):
        self.s = self.open_reqsession()

    def open_reqsession(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US;q=0.5,en;q=0.3',
            'Connection': 'keep-alive',
        }
        s = requests.session()
        s.headers = headers
        # s.proxies['http'] = 'http://35.240.8.116:8888'
        # s.proxies['https'] = 'https://35.240.8.116:8888'
        return s

    def load_url(self, url):

        if 'http' not in url:
            url = 'https://%s' % url
        # if 'detail' not in url:
        #     raise Exception('No "detail" domen in url.')

        errors = 1
        while errors > 0 and errors <= 10:
            try:
                print("Loading url %s..." % (url))
                r = self.s.get(url, timeout=60)
                errors = 0
            except Exception as e:
                print(url, 'Retrying...')
                errors += 1

        if errors != 0:
            print("Can't load %s" % url)
            return 0
        else:
            return r

    def get_images_url(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        url = soup.find(id="desc-lazyload-container")['data-tfs-url']

        context = self.load_url(url)
        soup = BeautifulSoup(context.text, 'html.parser')

        srcs = [img['src'] for img in soup.find_all('img')]

        return srcs

    def download_images(self, srcs, _dir):
        i = 1
        for src in srcs:

            src = re.search("/(.*)$", src).group()
            src = re.search("(.*?(?:jpg|png|jpeg))|.*", src).group()
            src = "https:%s" % (src)

            out = "%s/%d.jpg" % (_dir, i)

            print("Saving %s as %i.jpg" % (src, i))

            urllib.request.urlretrieve(src, out)

            im = Image.open(out)
            width, height = im.size
            im.close()

            if width < 500 or height < 500:
                print('Image too small...')
                os.remove(out)
            else:
                i = i + 1


if __name__ == '__main__':
    if len(sys.argv) == 3:
        _url = sys.argv[1]
        _dir = sys.argv[2]

        if os.path.isdir(_dir):
            print('Directory exists! Please type in a new directory name to prevent mishmash')
        else:
            os.makedirs(_dir, exist_ok=False)

            downloader = Downloader()
            response = downloader.load_url(_url)
            srcs = downloader.get_images_url(response)
            downloader.download_images(srcs, _dir)
