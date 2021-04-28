import unittest
import requests

from common.logger import Log
from api.foodshop import FoodShop

class TestFoodShop(unittest.TestCase):
    log = Log()

    def setUp(self) -> None:
        s = requests.session
        self.food_shop = FoodShop(s)

    def test_get_category(self):
        self.log.info("----start----")
        res = self.food_shop.get_foodroom_category()
        self.log.info("----调用结果:" + str(res))
        self.assertEqual(res["BusinessResponse"]["Result"], "SUCCESS")
        self.log.info("----end----")

    def test_get_article(self):
        self.log.info("----start----")
        res = self.food_shop.get_foodroom_article()
        self.log.info("----调用结果:" + str(res))
        self.assertEqual(res["BusinessResponse"]["Result"], "SUCCESS")
        self.log.info("----end----")

    def test_get_remarkmap(self):
        self.log.info("----start----")
        res = self.food_shop.get_foodroom_remarkmap()
        self.log.info("----调用结果:" + str(res))
        self.assertEqual(res["Result"], "SUCCESS")
        self.log.info("----end----")

    def test_get_remark(self):
        self.log.info("----start----")
        res = self.food_shop.get_foodroom_remark()
        self.log.info("----调用结果:" + str(res))
        self.assertEqual(res["BusinessResponse"]["Result"], "SUCCESS")
        self.log.info("----end----")