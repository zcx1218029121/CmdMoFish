from view.ErroTip import ErroTip
from view.TestListView import TestListView
from view.ViewGroup import ViewGroup
import requests


class Pager(ViewGroup):
    def creat(self):
        self.data = requests.get(url="https://www.tophub.fun:8888/v2/GetAllInfoGzip?id=60&page=0").json()["Data"][
            "data"]
        self.add_child(TestListView(self.data))
        self.add_child(ErroTip())
        self.add_child(ErroTip())
        self.add_child(ErroTip())
        self.add_child(ErroTip())
        self.add_child(ErroTip())


