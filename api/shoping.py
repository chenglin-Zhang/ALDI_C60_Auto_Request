import requests

from common.logger import Log


class Blog():
    log = Log()

    def __init__(self, s):
        self.s = s


    def get_shop_img(self):
        url = "http://10.1.23.245:9221/image/getImageFromFileAsJson"
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        params = {
            "Path": "C:\\TPDotnet\\Pictures\\Customer",
            "FileName": "10000001.jpg"
        }
        res = requests.get(url=url,headers=headers, params=params)
        return res.json()


if __name__ == '__main__':
    blog = Blog(requests.session())
    img = blog.get_shop_img()
    print(img.json())
