from view.ListView import ListView
from view.Pager import Pager
from view.Tip import Tip

import requests


class ListPager(Pager):
    """
    示例
    """

    def creat(self, param):
        self.p = 0
        self.data = \
            requests.get(url="https://www.tophub.fun:8888/v2/GetAllInfoGzip?id=58&page=0").json()["Data"][
                "data"]
        self.list_view = ListView(self.data)
        self.add_child(self.list_view)

    def handle_key(self, key):
        if "n" == key and self.list_view.isEnd:
            self.p = self.p + 1
            self.list_view.index = 0
            self.list_view.isEnd = False
            self.list_view.data = \
                requests.get(url="https://www.tophub.fun:8888/v2/GetAllInfoGzip?id=58&page=" + str(self.p)).json()[
                    "Data"][
                    "data"]
            return True
        if "b" == key:
            self.context.finish()
