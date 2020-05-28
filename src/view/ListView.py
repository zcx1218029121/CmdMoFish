from Stack import Stack
from view.Item import Item
from view.ViewGroup import ViewGroup


class ListView(ViewGroup):

    def creat(self, param):
        """
        在creat 中处理数据
        :return:
        """
        self.index = 0
        if len(self.data) == 0:
            self.isEnd = True
        else:
            self.isEnd = False

    def on_resume(self):

        self.child = []
        if self.index + self.show_count() < len(self.data):
            for i in range(self.index, self.index + self.show_count()):
                self.add_child(self.build_item(self.data[i]))
        else:
            self.isEnd = True
            for i in range(self.index, len(self.data)):
                self.add_child(self.build_item(self.data[i]))

    def handle_key(self, key):
        """
        处理输入事件
        :param key:
        :return:
        """
        if "n" == key:
            self.index = self.index + self.show_count()
        return False

    def stop_dispatch(self):
        """
        为减少数组递归分发的时间复杂度 拦截事件的分发
        :return: 是否消费当前输入
        """
        return True

    def build_item(self, data):
        return Item(data)

    def show_count(self):
        return 1
