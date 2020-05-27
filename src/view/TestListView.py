from view.Item import Item
from view.ListView import ListView
import requests


class TestListView(ListView):
    def build_item(self, data):
        return Item(data)

    def after_print(self):
        print("-------------------------")
