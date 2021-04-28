import requests

from common.logger import Log


class FoodShop():
    log = Log()

    def __init__(self, s):
        self.s = s
        self.host = "http://10.1.23.245:9221/tpdotnet/pos/webapi/"


    def get_foodroom_category(self):
        """
        美食工坊大类
        :return:
        """
        url = self.host+"aco-get-foodroom-category"
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        data = {
         "ClientId":"webapi",
         "Workflow":"aco-get-foodroom-category"
        }
        result = requests.post(url=url, headers=headers, json=data)
        return result.json()

    def get_foodroom_article(self, szCategoryID="5603"):
        """
        美食工坊商品
        :param szCategoryID: 大类ID
        :return:
        """
        url = self.host+"aco-get-foodroom-article"
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        data = {
         "ClientId":"webapi",
         "Workflow":"aco-get-foodroom-article",
         "szCategoryID": szCategoryID
        }
        result = requests.post(url=url, headers=headers, json=data)
        return result.json()


    def get_foodroom_remarkmap(self, szItemLookupCode=""):
        """
        美食工坊属性
        :param szItemLookupCode: 商品ID（可选）
        :return:
        """
        url = self.host+"aco-get-foodroom-remarkmap"
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        data = {
            "ClientId":"webapi",
            "Workflow":"aco-get-foodroom-remarkmap",
            "szItemLookupCode": szItemLookupCode
        }
        result = requests.post(url=url, headers=headers, json=data)
        return result.json()

    def get_foodroom_remark(self, szCategoryID="", szItemLookupCode=""):
        """
        美食工坊规格
        :param szCategoryID: 类别ID（可选）
        :param szItemLookupCode: 商品条码（可选）
        :return:
        """
        url = self.host+"aco-get-foodroom-remark"
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        data = {
            "ClientId": "webapi",
            "Workflow": "aco-get-foodroom-remark",
            "szCategoryID": szCategoryID,
            "szItemLookupCode": szItemLookupCode
        }
        result = requests.post(url=url, headers=headers, json=data)
        return result.json()


if __name__ == '__main__':
    blog = FoodShop(requests.session())
    img = blog.get_foodroom_category()
    img1 = blog.get_foodroom_article("4302")
    img2 = blog.get_foodroom_remarkmap()
    img3 = blog.get_foodroom_remark()
    print(img)
    print(img1)
    print(img2)
    print(img3)