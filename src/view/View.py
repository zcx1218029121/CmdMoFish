# coding=utf-8


class View:

    def __init__(self, data):
        self._data = data
        self.creat()

    def before_print(self):
        pass

    def after_print(self):
        pass

    def print_content(self):
        """
        打印
        :return:
        """
        pass

    def creat(self):
        """
        创建回调
        :return:
        """
        pass

    def resume(self):
        """
        激活回调
        :return:
        """
        self.before_print()
        self.print_content()
        self.after_print()

    def destroy(self):
        """
        销毁回调
        :return:
        """
        pass

    def handle_key(self, key):
        """
        处理事件默认消耗
        :param key:
        :return:
        """
        return True

    def dispatch_key(self, key):
        return self.handle_key(key)

    def set_data(self, data):
        self._data = data
        self.resume()

    def get_data(self):
        return self._data
