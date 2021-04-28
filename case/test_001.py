import unittest
import requests

from api.shoping import Blog
from common.logger import Log

class Test(unittest.TestCase):
    log = Log()

    def setUp(self) -> None:
        s = requests.session()
        self.blog = Blog(s)

    def test_get_img(self):
        '''测试获取商品图片案例'''
        self.log.info("----start----")
        result = self.blog.get_shop_img()
        print(result)
        print(result["ContentType"])
        self.log.info("----调用结果：" + str(result))
        self.log.info("----是否成功获取图片：" + result["ContentType"])
        self.assertEqual(result["ContentType"], "image/jpeg")
        self.log.info("----end----")
