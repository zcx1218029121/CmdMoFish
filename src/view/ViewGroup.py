from view.View import View


class ViewGroup(View):
    def __init__(self, data=None):
        self.child = None
        super().__init__(data)


    def add_child(self, view):
        if self.child is None:
            self.child = []

        self.child.append(view)

    def print_content(self):
        self.print_child()

    def print_child(self):

        for temp in self.child:
            temp.resume()

    def handle_key(self, key):
        """
        处理输入事件 默认消耗
        :param key:
        :return:
        """
        return True

    def dispatch_key(self, key):
        if self.stop_dispatch():
            return self.handle_key(key)

        for child_view in self.child:
            # 有一个子view 消费了当前事件 立即结束事件的分发
            if child_view.dispatch_key(key):
                return True
        return self.handle_key(key)

    def stop_dispatch(self):
        """
        是否拦截事件分发
        :return:
        """
        return False
