from Stack import Stack
from view.Item import Item
from view.ViewGroup import ViewGroup


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


class ListView(ViewGroup):

    def creat(self):

        for item_data in self.data:
            self.add_child(self.build_item(item_data))

    def handle_key(self, key):
        """
        处理输入事件
        :param key:
        :return:
        """
        if is_number(key):
            return True
        return False

    def stop_dispatch(self):
        """
        为减少数组递归分发的时间复杂度 拦截事件的分发
        :return: 是否消费当前输入
        """
        return True


    def build_item(self, data):
        pass
